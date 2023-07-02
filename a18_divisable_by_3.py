# 18. Write a python script to print the numbers which are divisible by 3 between two limits

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

print(f"Numbers divisible by 3 between {lower_limit} and {upper_limit}:")
for number in range(lower_limit, upper_limit + 1):
  if number % 3 == 0:
    print(number, end=" ")
print()