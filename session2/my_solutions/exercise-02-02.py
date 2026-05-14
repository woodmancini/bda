import json
import csv
import os
from pathlib import Path

SESSION_2_DIR = Path(__file__).parent.parent
DATA_DIR = SESSION_2_DIR / "data"

movies = [
    {
        "title": "Howl's Moving Castle",
        "year": "2004",
        "director": "Hayao Miyazaki",
        "music_by": "",
    },
    {
        "title": "Kiki's Delivery Service",
        "year": "",
        "director": "Hayao Miyazaki",
        "music_by": "Joe Hisaishi",
    },
]

for i, movie in enumerate(movies, start=1):
    for key, value in movie.items():
        if value.strip() == "":
            print(f"Record {i} missing field {key}")

original_movies = [movie.copy() for movie in movies]
cleaned_movies = [movie.copy() for movie in movies]

if cleaned_movies[0]["music_by"].strip() == "":
    cleaned_movies[0]["music_by"] = "Joe Hisaishi"

if cleaned_movies[1]["year"].strip() == "":
    cleaned_movies[1]["year"] = "1989"

print("Original:", original_movies)
print("Cleaned:", cleaned_movies)

with open("movies_clean.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_movies, file, ensure_ascii=False, indent=2)

print("Saved: movies_clean.json")

rows = []
with open(DATA_DIR / "studio_ghibli_movies.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    if not fieldnames:
        print("No header fields found!")
    
    for row in reader:
        rows.append(row)

for i, row in enumerate(rows, start=2):
    for column, value in row.items():
        if value is None or value.strip() == "":
            print(f"\nMissing field {column} in row number {i}: {row["title"]}.")

if rows[3]["music_by"] is None or rows[3]["music_by"].strip() == "":
    rows[3]["music_by"] = "Joe Hisaishi"

if rows[4]["year"] is None or rows[4]["year"].strip() == "":
    rows[4]["year"] = "1989"

if rows[6]["year"] is None or rows[6]["year"].strip() == "":
    rows[6]["year"] = "2008"

print("\nCleaned rows:", rows)
year_total = 0
year_count = 0
miyazaki_count = 0
for i, row in enumerate(rows):
        try:
            year = int(row["year"].strip())
            print(year)
            year_total += year
            year_count += 1
        except ValueError:
            print(f"Error converting year to int in row {i}.")

        if "Miyazaki" in row["director"]:
            miyazaki_count += 1

average_year = year_total // year_count
print(f"Average release year: {average_year}, and {miyazaki_count} films were directed by Miyazaki.")

with open("studio_ghibli_movies_clean.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
print(f"Saved cleaned dataset to: {os.getcwd()}\studio_ghibli_movies_clean.csv")

with open("studio_ghibli_movies_clean.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    if not fieldnames:
        print("No header fields found in cleaned file!")
    
    for i, row in enumerate(reader, start=2):
        for column, value in row.items():
            if value is None or value.strip() == "":
                print(f"\nMissing field {column} in row number {i}: {row['title']}.")