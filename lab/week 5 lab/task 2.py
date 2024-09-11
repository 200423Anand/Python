list1 = ["plum", "kiwi", "cherry"]
list2 = [1, 2, 3]
myset = set(list1 + list2)
myset.add(4)
myset.discard("apple")
newset = set(list(myset)[:3])
print("Values which is not in both sets:", myset.symmetric_difference(newset))
for value in myset.union(newset):
    print(value)