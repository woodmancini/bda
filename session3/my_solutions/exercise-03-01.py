TEXT_FILE = "les_miserables.txt"
target = "Jean"

def non_empty_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line

count = 0
for line in non_empty_lines(TEXT_FILE):
    if target in line:
        count += 1

print(count)