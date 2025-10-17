# Input from user selling price and purchase price
sp = int(input("Enter Selling Price: "))
pp = int(input("Enter Purchase Price: "))

# Calculate the difference
diff = sp - pp

# Determine profit, loss, or no gain
if sp > pp:
    print("Profit:₹",diff)
elif sp < pp:
    print("Loss: ",diff)
else:
    print("No Profit, No Loss.")
