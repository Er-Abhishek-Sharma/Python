# Ask the user to enter three numbers
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

# Determine and display the greatest number
if n1 >= n2 and n1 >= n3:
    print("The greatest number is :",n1)
elif n2 >= n1 and n2 >= n3:
    print("The greatest number is :",n2)
else:
    print("The greatest number is :",n3)
