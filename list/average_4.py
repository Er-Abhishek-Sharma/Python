# Create a program to find the average of a list of 10 numbers (without using library functions)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original list:", n)

total = 0
for i in range(len(n)):
    total += n[i]

average = total / len(n)
print("Average of the list is:", average)
