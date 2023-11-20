# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

#to calculate total height  
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

#to calculate total number of student
numberOfStudents = 0
for student in student_heights:
  numberOfStudents = numberOfStudents + 1
print(f"number of students = {numberOfStudents}")

#to calculate average height
average_height = round(total_height / numberOfStudents)
print(f"average height = {average_height}")  
  
