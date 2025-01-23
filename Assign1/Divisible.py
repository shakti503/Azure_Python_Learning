#Write a program that takes two numbers and checks if the first number is divisible by the second. If not, print the remainder.

num1 = int(input("enter a number:"))
num2 = int(input("enter second number:"))

if num1%num2==0:
    print(f"{num2} is a divisor of {num1}")
else:
    remainder = num1%num2
    print(f"Remainder is {remainder}")