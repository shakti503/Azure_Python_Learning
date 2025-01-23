flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Salted Caramel', 'Matcha', 'Rainbow Sherbet', 'Bubblegum', 'Cotton Candy'] 
sorted_flavors = sorted(flavors)
print(f"Sorted flavors: {sorted_flavors}")

base = {
    "single scoop": 3,
    "double scoop": 5.5,
    "triple scoop": 7.5
}

toppings = {
    "chocolate chips": 0.5,
    "Whipped Cream": 0.75,
    "Gummy Bears": 1
}

for value in base.values():
    total_cost = value+toppings['chocolate chips']+toppings['Whipped Cream']+toppings['Gummy Bears']
    print("total cost is", total_cost)


base_icecream = {3,5.5,7.5}

cheap = min(base_icecream)
print(f"Cheapest is {cheap}")
expensive = max(base_icecream) 
print(f"Costliest is {expensive}")
