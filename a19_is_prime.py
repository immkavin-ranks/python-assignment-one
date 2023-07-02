# 19. Write a python script to print prime or not


def is_prime(number):
  if number <= 1:
    return False

  for i in range(2, number):
    if number % i == 0:
      return False

  return True


number = int(input("Enter a number: "))
if is_prime(number):
  print(f"{number} is a prime number.")
else:
  print(f"{number} is not a prime number.")
