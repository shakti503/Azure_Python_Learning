"""Write a function summarize_items that performs the following:
	1.	Accepts at least one positional argument, which is the name of the person.
	2.	Accepts an arbitrary number of items (e.g., integers, strings, etc.) using *args.
	3.	Accepts arbitrary keyword arguments (e.g., metadata like date or location) using **kwargs.
	4.	The function should:
	•	Print the person’s name.
	•	Print the total number of items passed via *args.
Return a dict with all items in keywords args"""


def show(name, *args, **kwargs):
    print(f"name is {name} and pass marks are {args} and consecutive marks are {kwargs}")

show("shakti", 40,60,39, science=45,Maths=70,Social=75)





