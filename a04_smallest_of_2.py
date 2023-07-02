# 04. Write a python script to find the smallest of two numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

smallest = num1  # Assume num1 is the smallest initially

if num2 < smallest:
  smallest = num2

print(f"The smallest number is: {smallest}")
