given_inventory = {
    "Fruits": {"apple": 10, "plum": 20},
    "Vegetables": {"carrot": 5, "broccoli": 15},
    "Dairy": {"milk": 50, "cheese": 40}
}
vendor_inventory = {
    "Fruits": {"orange": 10, "grapes": 10},
    "Vegetables": {"raddish": 5, "spinach": 15},
    "Dairy": {"milk": 30, "yogurt": 50}
}
print("Items I have but vendor does not have:")
for category, items in given_inventory.items():
    for item, quantity in items.items():
        if item not in vendor_inventory[category]:
            print(item)
print("Items both I and vendor have:")
for category, items in given_inventory.items():
    for item, quantity in items.items():
        if item in vendor_inventory[category]:
            print(item)
item = input("Enter an item: ")
in_stock = False
for category, items in given_inventory.items():
    if item in items:
        in_stock = True
        break
print(f"Item '{item}' is in stock: {in_stock}")
vendor_has_item = False
for category, items in vendor_inventory.items():
    if item in items:
        vendor_has_item = True
        break
print(f"Vendor has item '{item}': {vendor_has_item}")