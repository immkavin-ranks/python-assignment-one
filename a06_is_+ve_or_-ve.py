# 06. Write a python script to find positive or negative

number = float(input("Enter a number: "))

if number > 0:
  print(f"{number} is positive.")
elif number < 0:
  print(f"{number} is negative.")
else:
  print("The number is zero.")
