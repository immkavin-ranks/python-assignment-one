# 17. Write a python script to print the odd numbers between two limits
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

print(f"Odd numbers between {lower_limit} and {upper_limit}:")
for number in range(lower_limit, upper_limit + 1):
  if number % 2 != 0:
    print(number, end=" ")
print()