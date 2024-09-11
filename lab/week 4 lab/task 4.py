mylist = []
for _ in range(5):
    user = input("Enter a value: ")
    if user not in mylist:
        mylist.append(user)

print("mylist:", mylist)
