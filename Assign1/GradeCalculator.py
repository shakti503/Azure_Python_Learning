'''Write a program that takes a score (0 to 100) from the user and assigns a grade:
90-100: Grade A
80-89: Grade B
70-79: Grade C
60-69: Grade D
Below 60: Grade F'''

marks = int(input("enter the student marks: "))
if marks>=90 and marks<=100:
    print("Student scored Grade A")
elif marks>=80 and marks<=89:
    print("Student scored Grade B")
elif marks>=70 and marks<=79:
    print("Student scored Grade C")
elif marks>=60 and marks<=69:
    print("Student scored Grade D")
else:
    print("Student scored Grade F")

