'''Check Eligibility to Vote
Write a program that asks for the user’s age and checks if they are eligible to vote. Assume the voting age is 18 or older.'''

age = int(input("enter the voters age:"))
flag = -1
if age>=18 and age<=100:
    print(f"Voter of age {age} is eligible to vote")
elif age>flag and age<18:
    print(f"Voter of age {age} is not eligible for voting")
else:
    print(f"{age} is an invalid entry")

