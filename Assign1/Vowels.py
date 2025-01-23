#Write a program that checks if a given character is a vowel (a, e, i, o, u) or a consonant. Assume the input is a single letter.

letter = input("Enter a letter:")
nums = ['a', 'e', 'i', 'o', 'u']
for char in nums:
    if char == letter:
     print(f"entered letter {letter} is a vowel")
     break
else:
    print(f"entered letter {letter} is a not vowel")

