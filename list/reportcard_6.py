"""Create a reportcard . It must contain the name of five subjects along with marks obtained in 
them out of 100.
Then calculate the total marks obtained, percentage, grade.
Grade must be calculated as per below criteria :-
Percentage           Grade
>=85                      A+
85 - 75                   A
75-65                     B
65 - 55                   C
55 - 50                   D
<50                       Fail"""

# Report Card Generator for 5 Subjects

# Empty list to store [subject, marks] pairs
subjects = []

print("Enter the name and marks (out of 100) for five subjects:")

# Collect subject names and marks
for i in range (5): 
  name = input("Enter subject name : ")
  marks = int(input("Enter subject marks : ")) 
  
  # Check if input within 0-100
  if 0 <= marks <= 100:
    subjects.append([name, marks])
  else:
    print("Marks must be between 0 and 100. Setting marks to 0.")
    subjects.append([name, 0])
    

# Display entered data
print("\n------------------- Report Card -------------------")
total = 0
for i in range(5): 
  total += marks

# Calculate percentage
percentage = total*100 / 500

# Determine grade
if percentage >= 85:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 65:
    grade = "B"
elif percentage >= 55:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

# Final Output
print("----------------------------------------------------")
print(f"Total Marks      : {total} / 500")
print(f"Percentage       : {percentage:.2f}%")
print(f"Grade            : {grade}")
print("----------------------------------------------------")
