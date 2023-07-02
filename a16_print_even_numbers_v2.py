# 16. Write a python script to print the even numbers between two limits

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

print(f"Even numbers between {lower_limit} and {upper_limit}:")
for number in range(lower_limit, upper_limit + 1):
  if number % 2 == 0:
    print(number, end=" ")
print()
