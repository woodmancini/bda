from library import ask_gemini
from pathlib import Path
import csv

SESSION2_DIR = Path(__file__).parent.parent
DATA_DIR = SESSION2_DIR / "data"

rows_list = []
missing_fields = []
missing_count = 0

# Find rows with missing year
with open(DATA_DIR / "studio_ghibli_movies.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    header = reader.fieldnames
    for i, row in enumerate(reader):
        rows_list.append(row)
        #if row["year"] is None or row["year"].strip() == "":
        for column, value in row.items():
            if value is None or value.strip() == "":
                missing_fields.append((row["movie_id"], row["title"], column))
                missing_count += 1


print(f"{missing_count} fields missing:\n{missing_fields}")

for item in missing_fields:
    line, title, field = item
    try:
        index = int(line.strip()) - 1
    except ValueError:
        print("Can't parse movie_id.")

    if field == "year":
        answer = ask_gemini(f"""Return only the 4-digit release year for the Studio Ghibli movie {title}.
Output format: name only, no extra text.""")
        rows_list[index]["year"] = answer

    elif field == "music_by":
        answer = ask_gemini(f"""Return only the composer full name for the Studio Ghibli movie {title}.
Output format: name only, no extra text.""")
        rows_list[index]["music_by"] = answer
    
for row in rows_list:
    print(row["year"])
    print(row["music_by"])

with open(DATA_DIR / "SG_movies_gemini_cleaned.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(rows_list)

print(f"Saved cleaned and updated file to {DATA_DIR / 'SG_movies_gemini_cleaned.csv'}.")