def count_elements(data):
    count = 0
    for item in data:
        if 0 < item < 11:
            count += 1
    return count

def sum_even_numbers(data):
    total = 0
    for item in data:
        if item % 2 == 0:
            total += item
    return total

def find_12(data):
    for i in range(len(data)):
        if data[i] == 12:
            return i
    return -1

# Only returns first match
def find_in_matrix(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 25:
                return(f"[{i + 1},{j + 1}]")

data = [10, 20, 30, 40, 50, 12, 5, 9]
matrix = [
    [5, 10, 15],
    [20, 25, 10, 25]
]
print(count_elements(data))
print(sum_even_numbers(data))
print(find_12(data))
print(find_in_matrix(matrix))