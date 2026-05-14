import csv 
from pathlib import Path

DIR_PATH = Path(__file__).parent

with open(DIR_PATH / "movies.csv", "r", newline = "", encoding="utf-8") as file:
    
    reader = csv.reader(file)

    dict_reader = csv.DictReader(file)

# Print header only
    header = next(reader)
    print("HEADER\n")
    print(header)

# Print first five rows
    counter = 0
    for row in reader:
        if counter < 5:
            print(row)
        else:
            break
        counter += 1

    file.seek(0)
# Or
    print("ENUMERATE\n")
    for i, row in enumerate(reader):
        if i < 5:
            print(row)

# Print reader object
    print(reader)

    file.seek(0)

# Print 5th column (if it exists
    for row in reader:
        if len(row) > 4:
            print(row[4])

    file.seek(0)

# Finding "Action" with reader
    genre_index = header.index("genres")
    for row in reader:
        if "Action" in row[genre_index]:
            print("ACTION MOVIE",row)
            break

    file.seek(0)

# Or with 'generator expression'
    action_movie_1 = next((row for row in reader if "Action" in row[genre_index]), None)
    print(action_movie_1)

    file.seek(0)

# DictReader prints first row with Action genre
    for row in dict_reader:
        if "Action" in row["genres"]:
            print(row)
            break

    file.seek(0)

# Or with 'generator expression'
    first_action_movie = next((row for row in dict_reader if "Action" in row["genres"]), None)
    print(first_action_movie)

with open(DIR_PATH / "movies_incomplete.csv", "r", newline = "", encoding = "utf-8") as file:
    reader = csv.DictReader(file)
    
    for i, row in enumerate(reader, start=2):
        for column, value in row.items():
            if value is None or value.strip() == "":
                print(f"Error: empty field in row {i}, column '{column}'.")