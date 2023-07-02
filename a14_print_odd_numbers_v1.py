# 14. Write a python script to print the odd numbers within n using loop

n = int(input("Enter a number: "))
counter = 1

print(f"Odd numbers within {n}:")
while counter <= n:
  if counter % 2 != 0:
    print(counter, end=" ")
  counter += 1
print()