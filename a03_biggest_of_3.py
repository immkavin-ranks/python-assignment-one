# 03. Write a python script to find the biggest of three numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

biggest = num1  # Assume num1 is the biggest initially

if num2 > biggest:
  biggest = num2

if num3 > biggest:
  biggest = num3

print(f"The biggest number is: {biggest}")
