my_inventory = {
    "Fruits": {"orange": 15, "Gava": 22},
    "Vegetables": {"Celery": 10, "cauliflower": 8},
    "Dairy": {"milk": 50, "cheese": 40, "eggs": 100}
}
vendor_inventory = {
    "Fruits": {"kiwi": 10, "pear": 26},
    "Vegetables": {"carrot": 23, "cabbage": 10},
    "Dairy": {"milk": 20, "yogurt": 16}
}
print("Items I have but vendor does not have:")
for category, items in my_inventory.items():
    for item, quantity in items.items():
        if item not in vendor_inventory[category]:
            print(item)
print("Items both I and vendor have:")
for category, items in my_inventory.items():
    for item, quantity in items.items():
        if item in vendor_inventory[category]:
            print(item)
item = input("Enter an item: ")
in_stock = False
for category, items in my_inventory.items():
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