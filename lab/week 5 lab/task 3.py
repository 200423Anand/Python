my_dictionary = {"name": "Perminder Kaur", "age": 20, "city": "Mississauga"}
print("Value of 'name' key:", my_dictionary["name"])
del my_dictionary["age"]
for key, value in my_dictionary.items():
    print(f"{key} = {value}")