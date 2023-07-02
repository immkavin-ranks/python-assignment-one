def is_prime(number):
  if number <= 1:
    return False

  for i in range(2, number):
    if number % i == 0:
      return False

  return True


lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

print(f"Prime numbers between {lower_limit} and {upper_limit}:")
for number in range(lower_limit, upper_limit + 1):
  if is_prime(number):
    print(number, end=" ")
print()
