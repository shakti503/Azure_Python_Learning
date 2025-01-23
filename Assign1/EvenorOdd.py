#1. Odd or Even
#Write a program that takes an integer input from the user and checks if it is odd or even.

nums = int(input("enter a number: "))
print("entered number is", nums)
if nums%2 == 1:
    print("entered number is odd")
else:
    print("number is even")
