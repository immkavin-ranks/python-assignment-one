# 12. Write a python script to print Mark List

mark_list = []

while True:
  student_name = input("Enter the name of the student (or 'q' to quit): ")
  if student_name == 'q':
    break

  student_marks = float(input("Enter the marks of the student: "))

  mark_list.append((student_name, student_marks))

print("Mark List:")
for student_name, student_marks in mark_list:
  print(f"Name: {student_name}, Marks: {student_marks}")
