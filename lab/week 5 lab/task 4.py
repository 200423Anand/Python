list1 = ["plum", "kiwi", "cherry"]
list2 = [1, 2, 3]
mydict = dict(zip(list1, list2))
for key, value in mydict.items():
    print(f"{key} = {value}")