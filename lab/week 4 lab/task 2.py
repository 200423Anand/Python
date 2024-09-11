mylist = ["apple", "banana", "cherry"]
mylist.append("plum")
mylist.pop(0)
checking = "cherry"
if checking in mylist:
    print(f"'{checking}' exists in the list at index:", mylist.index(checking))
else:
    print(f"'{checking}' is not in the list")
