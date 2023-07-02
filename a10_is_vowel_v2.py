# 10. Write a python script to check the given character is vowel or not


def is_vowel(char):
  vowels = ['a', 'e', 'i', 'o', 'u']
  if char.lower() in vowels:
    return True
  else:
    return False


character = input("Enter a character: ")

if len(character) == 1:
  if is_vowel(character):
    print(f"{character} is a vowel.")
  else:
    print(f"{character} is not a vowel.")
else:
  print("Please enter a single character.")
