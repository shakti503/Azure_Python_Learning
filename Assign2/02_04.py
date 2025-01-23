flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Salted Caramel', 'Matcha', 'Rainbow Sherbet', 'Bubblegum', 'Cotton Candy'] 

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

prepackaged = {
    "ice cream bars": 2.5,
    "popsicles": 2,
    "mini tubs": 3.5
}

for key in toppings:
    print(f"cost if customer opts single scoop with {key} is {toppings[key]+ base['single scoop']} ")
    print(f"cost if customer opts double scoop with {key} is {toppings[key]+ base['double scoop']} ")
    print(f"cost if customer opts triple scoop with {key} is {toppings[key]+ base['triple scoop']} ")

