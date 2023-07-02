# 22. Write a python script to print the Fibonacci series


def fibonacci(n):
  a, b = 0, 1

  if n <= 0:
    print("Invalid input. Please enter a positive integer.")
  elif n == 1:
    print(a)
  else:
    print(a, end=" ")
    print(b, end=" ")

    for _ in range(2, n):
      c = a + b
      print(c, end=" ")
      a, b = b, c
    print()


number_of_terms = int(input("Enter the number of terms: "))
fibonacci(number_of_terms)
