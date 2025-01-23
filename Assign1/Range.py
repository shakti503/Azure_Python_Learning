##Write a program that checks if a number is within a specific range. Ask the user to input the number, as well as the start and end of the range. Print "In range" if the number is within the range, otherwise print "Out of range".

number = int(input("Enter a number:"))
bound1 = int(input("Enter the lower bound:"))
bound2 = int(input("Enter the upper bound:"))
for num in range(bound1,bound2):
    if num == number:
        print(f"{number} is in range")
else:
    print(f"{number} is not in range")