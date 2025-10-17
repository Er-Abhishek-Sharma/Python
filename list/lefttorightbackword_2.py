# Create a list of 10 numbers
n = [30, 40, 90, 60, 20, 70, 10, 80, 20, 50]

print("Displaying elements left to right using backward indexing:")

for index in range(-len(n), 0):
    print(n[index], end=', ')
