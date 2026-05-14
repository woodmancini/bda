import csv
from pathlib import Path

SESSION_2_DIR = Path(__file__).parent.parent
DATA_DIR = SESSION_2_DIR / "data"

with open(DATA_DIR/"movies.csv", "r", newline="", encoding="utf-8") as file:

    count = 0

    dict_reader = csv.DictReader(file)

    for row in dict_reader:
        if row["year"] == "2020":
            count += 1
    
    print(f"Total movies released in 2020: {count}")

    file.seek(0)

    for row in dict_reader:
        if "Action" in row["genres"]:
            print(f"First action movie: {row["title"]}")
            break

    file.seek(0)

    fieldnames = dict_reader.fieldnames
    print(type(fieldnames))
    print(fieldnames)

    USA_count = 0
    for row in dict_reader:
        if "USA" in row["country"]:
            USA_count += 1
    
    print(f"Total films from USA: {USA_count}")

    file.seek(0)

    for row in dict_reader:
        if row["genres"] == "Action":
            print(f"First pure action film: {row["title"]}")
            break

    file.seek(0)

    for row in dict_reader:
        if "Action" in row["genres"] and row["genres"] != "Action":
            print(f"First mixed-genre action film: {row["title"]}")
            break

# DictReader allows easy access to fields based on the name given in the header row.

with open(DATA_DIR / "movies_incomplete.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames or []
        total_votes = 0.0
        vote_count = 0

        print("\nMissing data in incomplete dataset:")
        found_missing = False

        for line_number, row in enumerate(reader, start=2):
            for column in fieldnames:
                value = row.get(column)
                if value is None or value.strip() == "":
                    print(f"Missing cell at row {line_number}, column '{column}'")
                    found_missing = True

            try: 
                vote = float(row.get("votes"))
                total_votes += vote
                vote_count += 1
            except ValueError, TypeError:
                pass

        if not found_missing:
            print("No missing cells found.")

        average_votes = total_votes / vote_count

        print(f"Average votes is {average_votes:.2f} for a total of {vote_count} votes")