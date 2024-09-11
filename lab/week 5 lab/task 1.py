number_set1 = set(range(10, 21))
number_set2 = set(range(5, 16))
print("Difference is:", number_set1 - number_set2)
print("Common numbers are:", number_set1 & number_set2)
for num in number_set1:
    print("Set 1:", num)
for num in number_set2:
    print("Set 2:", num)