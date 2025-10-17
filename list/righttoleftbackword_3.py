# Create a list of 10 numbers
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Displaying elements from right to left using backward indexing:")

for index in range(-1, -len(n)-1, -1):
    print(n[index], end=', ')
