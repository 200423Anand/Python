def task1(arg1, arg2, arg3):

    return [type(arg1).__name__, type(arg2).__name__, type(arg3).__name__]


# Testing Task 1
print("Task 1:")
print("Case 1:", task1(1, "hi", 1.1))
print("Case 2:", task1(1, 2, 3))
print("Case 3:", task1("hello", "world", "python"))


def task2(text, num):

    if not isinstance(text, str) or not isinstance(num, int) or num < 2:
        return False
    return text * num


# Testing Task 2
print("\nTask 2:")
print("Case 1:", task2("Hello", -2))
print("Case 2:", task2("World", 5))
print("Case 3:", task2("Hello", "Bye"))
print("Case 4:", task2("Sky", 3))


def task3():

    print("First Name: Anand")
    return "Sharma"


# Testing Task 3
print("\nTask 3:")
print("Last Name:", task3())


def task4(num, factor):

    return num % factor == 0


# Testing Task 4
print("\nTask 4:")
print("Case 1:", task4(15, 5))

import re


def task5(postal_code):

    pattern = r'^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$'
    return bool(re.match(pattern, postal_code))


# Testing Task 5
print("\nTask 5:")
print("Case 1:", task5("M1S 3E6"))
print("Case 2:", task5("abc"))


def task6(first_name, last_name):

    return f"{last_name}, {first_name}"


# Testing Task 6
print("\nTask 6:")
print("Case 1:", task6("Anand", "Sharma"))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
