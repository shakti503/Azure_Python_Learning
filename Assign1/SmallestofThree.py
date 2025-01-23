'''Smallest of Three Numbers
Write a program that takes three numbers from the user and prints the smallest of the three.'''


num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

if num1<num2 and num2<num3:
    print(f"{num1} is smallest number")
elif num2<num1 and num2<num3:
    print(f"{num2} is smallest number")
else:
    print(f"{num3} is smallest number")