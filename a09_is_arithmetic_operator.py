# 09. Write a python script to check the given operator is arithmetic operator or not


def is_arithmetic_operator(operator):
  arithmetic_operators = ['+', '-', '*', '/', '%', '//', '**']
  if operator in arithmetic_operators:
    return True
  else:
    return False


operator = input("Enter an operator: ")

if len(operator) == 1:
  if is_arithmetic_operator(operator):
    print(f"{operator} is an arithmetic operator.")
  else:
    print(f"{operator} is not an arithmetic operator.")
else:
  print("Please enter a single operator.")
