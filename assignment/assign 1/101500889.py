"""
Assignment 1 File

Full Name:
Student Number: 101512849

Only edit the text where indicated
Make sure that the final result of the function is stored in the variable RESULT
"""


def task1(text1, text2, text3):
    """
    returns the text that is the longest. if there is a tie, concatenate the text(s), separated by underscores in the same order of the arguments

    >>> task1("hi", "bye", "hello")
    'hello'
    >>> task1("hello", "create", "every")
    'create'
    >>> task1("hi", "al", "oh")
    'hi_al_oh'
    >>> task1("two", "hi", "one")
    'two_one'
    >>> task1(" ", "  ", "   ")
    '   '
    """
    result = ''
    ########################
    # Start writing code
    ########################
    texts = [text1, text2, text3]
    max_length = max(len(text) for text in texts)
    longest_texts = [text for text in texts if len(text) == max_length]
    result = '_'.join(longest_texts)
    ########################
    # End writing code
    ########################
    return result


def task2(operand1, operator, operand2):
    """
    returns the result of an arithmetic operation. Accept the following four operators +, -, * & /.

    >>> task2(10, "+", 5)
    15
    >>> task2(10, "-", 5)
    5
    >>> task2("10", "*", 5)
    50
    >>> task2("10", "/", "5")
    2
    >>> task2("5", "-", 10)
    -5
    """
    result = 'false'
    ########################
    # Start writing code
    ########################
    try:
        operand1 = int(operand1)
        operand2 = int(operand2)

    except ValueError:
        return False

    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        if operand2 != 0:
            # Check if the division result is a whole number
            if operand1 % operand2 == 0:
                result = operand1 // operand2  # Integer division
            else:
                result = operand1 / operand2
        else:
            result = False
    ########################
    # End writing code
    ########################
    return result

def task3(name):
    """
    Determines if the name is valid. A valid name contains only one space and at least 5 characters
    >>> task3("foo")
    False
    >>> task3("having fun?")
    True
    >>> task3("Python Rocks")
    True
    >>> task3("Python is the best language")
    False
    >>> task3("a b")
    False
    """
    result = 'false'
    ########################
    # Start writing code
    ########################
    if name.count(' ') == 1 and len(name) >= 5:
        result = True
    ########################
    # End writing code
    ########################
    return result


def task4(value, multiplier):
    """
    returns either a string repeated X times or the product of two numbers (the arithmetic operation). Return False if the second argument is NOT a number
    >>> task4("hello", 3)
    'hellohellohello'
    >>> task4(10, 3)
    30
    >>> task4('10', 3)
    '101010'
    >>> task4('10', '3')
    False
    >>> task4('hi', '2')
    False
    """
    result = 'False'
    ########################
    # Start writing code
    ########################
    try:
        multiplier = int(multiplier)
    except ValueError:
        return False

    if isinstance(value, str):
        result = value * multiplier
    elif isinstance(value, int) and isinstance(multiplier, int):
        result = value * multiplier
    ########################
    # End writing code
    ########################
    return result