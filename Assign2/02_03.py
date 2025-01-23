classic = ['Vanilla','Chocolate Chips', 'Chocolate+CrushedOreos', 'Strawberry' ,'WhippedCream']
trendy = ['Matcha', 'white_chocolate_drizzle', 'cookies&cream' ]
kidfriendly = ['Bubblegum', 'cottoncandy', 'pop_rocks', 'gummy bears']

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Salted Caramel', 'Matcha', 'Rainbow Sherbet', 'Bubblegum', 'Cotton Candy'] 

flavor_req = input("Enter the flavor needed:")
if flavor_req in classic:
    print(f"Required flavor {flavor_req} is a classic type")
elif flavor_req in trendy:
    print(f"Required flavor {flavor_req} is a trendy type")
else:
    print(f"Required flavor {flavor_req} is a kidfriendly type")