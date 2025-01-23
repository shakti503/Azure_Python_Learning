nums = int(input("Enter a number:"))
if nums%4==0:
    print(f"{nums} is a leap year")
elif nums%100==0 and nums%400==0:
    print(f"{nums} is a leap year")
else:
    print(f"{nums} is not a  leap year")