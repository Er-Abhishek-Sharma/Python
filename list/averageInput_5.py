# Create a program to find out the average of 10 numbers given by the user

# Create an empty list
n = []

print("Enter any 10 numbers:")

# Input loop
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    n.append(num)

# Display the list
print("\nNumbers are:", n)

# Calculate sum of numbers
total = 0
for i in range(10):
    total += n[i]

# Calculate average
average = total / len(n)

# Display results
print("----------------------")
print("Sum is     :", total)
print("Average is :", average)
