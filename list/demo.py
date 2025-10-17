# Create a list of 20 numbers
numbers = n = [1,2,3,4,5,6,7,13,8,9,10,11,12,13,14,15,16,17,18,19]


print("Original List:", numbers)

# Take input from the user
num = int(input("Enter a number to remove its occurrences (except the first one): "))

# Flag to check first occurrence
found_first = False

# Create a new list
new_list = []
for n in numbers:
    if n == num:
        if not found_first:
            new_list.append(n)   # Keep the first occurrence
            found_first = True
        # Skip all other occurrences
    else:
        new_list.append(n)

print("Updated List:", new_list)
