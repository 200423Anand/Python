def task1(arg1, arg2, arg3):
    """

    >>> task1(1, "hi", 1.1)
    ['int', 'str', 'float']
    >>> task1("string", 2, 3.14)
    ['str', 'int', 'float']
    >>> task1(5, 10, 15)
    ['int', 'int', 'int']
    >>> task1("a", "b", "c")
    ['str', 'str', 'str']
    """
    return [type(arg1).__name__, type(arg2).__name__, type(arg3).__name__]


def task2(string_A, number_1):
    """
    >>> task2("Hello", -2)
    False
    >>> task2("World", 5)
    'WorldWorldWorldWorldWorld'
    >>> task2("Hello", "World")
    False

    """
    if not isinstance(string_A, str) or not isinstance(number_1, (int, float)):
        return False
    if number_1 < 2:
        return False
    return string_A * int(number_1)


def task3():

    first_name = "Perminder"
    last_name = "Kaur"
    print(first_name)
    return last_name


def task4(num1, num2):
    """

    >>> task4(3, 9)
    True
    >>> task4(4, 10)
    False
    """
    return num2 % num1 == 0

def task5(postal_code):
    """

    >>> task5("M1G 1W6")
    True
    >>> task5("123 ABC")
    False
    """
    import re
    pattern = re.compile(r"^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$")
    return bool(pattern.match(postal_code))


def task6(first_name, last_name):
    """


    >>> task6("Perminder", "Kaur")
    'Kaur, Perminder'
    """
    return f"{last_name}, {first_name}"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
