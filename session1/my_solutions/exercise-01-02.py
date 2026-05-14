from exercise_01_02_lib import my_len

print (my_len([10, 20, 30]))

data = [10, 20, 30, 40, 50]

total = 0

for item in data:
    total += item

print(total)

pointer = 0
for item in data:
    if item == 30:
        print(pointer)
        break
    pointer += 1

matrix = [
    [10, 20],
    [30, 40]
]

row_index = 0
col_index = 0

for row in matrix:
    print("Row:", row_index)
    for value in row:
        print("Column:", col_index, "Value:", value)
        col_index += 1
    col_index = 0
    row_index += 1

from tasks import count_elements
print(count_elements(data))