inventory = {
    "Laptop": 5,
    "Mouse": 20,
    "Keyboard": 10
}

print("Current Inventory")

for item, quantity in inventory.items():
    print(f"{item}: {quantity}")