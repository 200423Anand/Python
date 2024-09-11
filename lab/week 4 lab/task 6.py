num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))
num3 = int(input("Enter the increment number: "))
for i in range(0, num1 + 1):
    print(i)
for i in range(1, num1 + 1):
    print(i)
for i in range(num1, num2 + 1):
    print(i)
for i in range(num1, num2 + 1, num3):
    print(i)
