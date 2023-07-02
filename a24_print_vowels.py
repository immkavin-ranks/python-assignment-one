# 24. Write a python script to print the vowels without ‘i’

vowels = ['a', 'e', 'i', 'o', 'u']

print("Vowels without 'i':")
for vowel in vowels:
  if vowel != 'i':
    print(vowel, end="  ")
print()