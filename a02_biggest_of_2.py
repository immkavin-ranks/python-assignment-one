# 02. Write a python script to find the biggest of two numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

biggest = num1  # Assume num1 is the biggest initially

if num2 > biggest:
  biggest = num2

print(f"The biggest number is: {biggest}")
