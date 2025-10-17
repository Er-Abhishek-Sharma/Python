"""# Creating a list of 10 no.

n = [1,2,3,4,5,6,7,8,9,10]

# Displaying List
print("List is : ",n)

print("------------------------------------------------------------------------")

# removing 5th element

n.pop(4)
print("After removing list is : ",n)

# removing first occurence of 9 from list

print("------------------------------------------------------------------------")
n.remove(9)
print("Removing first occurence of 9 : ",n)

# To removing second element

print("------------------------------------------------------------------------")
del n[2]
print("After removing of the list : ",n)


# To removing range element

print("------------------------------------------------------------------------")
del n[1:3]
print("After removing of the list : ",n)

# To removing range step  element
n = [1,2,3,4,5,6,7,8,9,10]
print("------------------------------------------------------------------------")
del n[1:10:3]
print("After removing of the list : ",n)

# counting occurencde of 4
n = [1,2,3,4,5,6,7,8,9,10]
print("------------------------------------------------------------------------")
x=n.count(4)
print("Occurence of 4 : ",n)

# removing 4 from list 
print("------------------------------------------------------------------------")

for i in range(x):
  n.remove(4)
print("After removing of the list : ",n)"""

"""wap to create list of 20 no. and asked the user to input any no. 
and remove its all the occurences accepted first occurence"""

n = [1,2,3,4,5,6,7,13,8,9,10,11,12,13,14,15,16,17,18,19]
print(n)
print("------------------------------------------------------------------------")


num = int(input("Enter a number removed its occurrences (except the first one): "))

found_first=False

new_list=[]

for n in range(num):
  if n == num:
        if not found_first:
            new_list.append(n)   
            found_first = True
  else:
    new_list.append(n)



print("After the list : ",new_list)


