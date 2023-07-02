# 08. Write a python script to check the given character is vowel or not

vowels = {'a', 'e', 'i', 'o', 'u'}

character = input("Enter a character: ")

if len(character) == 1:
  if character.lower() in vowels:
    print(f"{character} is a vowel.")
  else:
    print(f"{character} is not a vowel.")
else:
  print("Please enter a single character.")
