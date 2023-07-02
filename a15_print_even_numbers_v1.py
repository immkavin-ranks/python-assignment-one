# 15. Write a python script to print the even numbers within n using while loop

n = int(input("Enter a number: "))
counter = 1

print(f"Even numbers within {n}:")
while counter <= n:
  if counter % 2 == 0:
    print(counter, end=" ")
  counter += 1
print()