import csv 
from pathlib import Path

DIR_PATH = Path(__file__).parent

with open(DIR_PATH / "movies.csv", "r", newline = "", encoding = "utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    total_rows = 0
    for row in reader:
        total_rows += 1
    
    print(f"\nTotal number of rows: {total_rows}\nNumber of columns: {len(header)}")

    file.seek(0)

    print("\nFirst three rows:")
    for i, row in enumerate(reader):
        if i < 3:
            print(row)
        else:
            break

    file.seek(0)

    genres_index = header.index("genres")
    print("\nFirst Action film:")
    for row in reader:
        if "Action" in row[genres_index]:
            print(row)
            break

    file.seek(0)

    dict_reader = csv.DictReader(file)
    ratings_total = 0
    valid_ratings_count = 0
    rated_above_8 = 0

    for row in dict_reader:
        try:
            rating = float(row["rating_imdb"])
            if rating >= 8:
                rated_above_8 += 1
            ratings_total += rating
            valid_ratings_count += 1
        except ValueError:
            pass

    if valid_ratings_count > 0:
        average = ratings_total / valid_ratings_count
        print(f"\nAverage IMDB rating is {average:.2f}, from a total of {valid_ratings_count} ratings.")
    else:
        print("No valid ratings found.")

    print(f"\nTotal films rated 8.0 or higher: {rated_above_8}")

    file.seek(0)

    mins_total = 0
    valid_runtime_count = 0
    for row in dict_reader:
        try:
            mins = float(row["runtime_min"])
            mins_total += mins
            valid_runtime_count += 1
        except ValueError:
            pass
    
    average_mins = mins_total / valid_runtime_count
    print(f"\nAverage runtime in minutes is {int(average_mins)}, from a total of {valid_runtime_count} entries.")

    # Complexity is O(n) for first-match search (worst case), and same for computing the average.