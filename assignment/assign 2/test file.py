"""
Assignment 2 File

Full Name: Jatin
Student Number: 101502440

Only edit the text where indicated
Make sure that the final result of the function is stored in the variable RESULT
"""


def task1(gross_salary):
    """
    Given the Federal Income Tax Rates chart located below,

    Tax rate    Taxable income threshold
    15%         $55,000 or less
    21%         $55,001 up to $111,000
    26%         $111,001 up to $173,000
    29%         $173,001 up to $246,000
    33%         $246,001 or higher

    Code the function that accepts ONE gross salary and returns net salary and tax rate as a string percent as a tuple:

    NOTE: you are required to add the neccessary paramaters, method body and return statement.
    NOTE: The method can accept string and int values (no float values)
    NOTE: the salary will only accept whole values for the gross salary value
    NOTE: the net value should be rounded to the nearest whole number. Remove all decimal values
    NOTE: error handling is not expected of you, assume that if the value passed is a string value, all characters will be 0-9
    >>> task1(100000)
    (79000, '21%')
    >>> task1(180000)
    (127800, '29%')
    >>> task1(250000)
    (167500, '33%')
    >>> task1('23456')
    (19938, '15%')
    >>> task1('55000')
    (46750, '15%')
    """
    ########################
    # Start writing code
    ########################
    # Ensure the salary is an integer
    gross_salary = int(gross_salary)

    if gross_salary <= 55000:
        tax_rate = 15
    elif gross_salary <= 111000:
        tax_rate = 21
    elif gross_salary <= 173000:
        tax_rate = 26
    elif gross_salary <= 246000:
        tax_rate = 29
    else:
        tax_rate = 33

    # Calculate net salary
    net_salary = gross_salary * (1 - tax_rate / 100)
    net_salary = round(net_salary)

    RESULT = (net_salary, f'{tax_rate}%')
    ########################
    # End writing code
    ########################
    return RESULT


def task2(monthly_budget, max_expense, expenses):
    """
    Code a function that accepts
        1) Accept a monthly budget value
        2) A maximum expense value
        3) A dictionary of expenses with the folllowing keys-value pair
            key = expense name: string value
            value = expense price: int/float value

        Iterate the dictionary of values and return one of the following values
            True & sum of all expenses: if the sum of all expenses is less than or equal to the monthly budget value
            False & sum of all expenses: if the sum of all expenses is greater than the monthly budget value
            False, the expense name & the expense value of the FIRST expense that is greater than the maximum expense value

    NOTE: you are required to add the neccessary paramaters, method body and return statement.
    NOTE: error handling is not expected of you, assume that if the values passed will be int, int and dictionary

    >>> task2(100, 40, {'food': 20, 'fun': 15, 'clothes': 30, 'travel': 25})
    (True, 90)
    >>> task2(150, 35, {'food': 30, 'books': 35, 'internet': 40, 'streaming services': 15})
    (False, 'internet', 40)
    >>> task2(180, 40, {'food': 30, 'fun': 25, 'clothes': 30, 'travel': 25, 'books': 35, 'internet': 40, 'streaming services': 15})
    (False, 200)
    >>> task2(300, 50, {'coat': 30, 'jeans': 20, 'hat': 15, 'scarf': 10, 'boots': 40, 'socks': 5, 'food': 20, 'fun': 15, 'clothes': 30, 'travel': 25})
    (True, 210)
    >>> task2(500, 100, {'coffee': 40, 'restaurant': 200, 'travel': 50, 'plan ticket': 350, 'school': 90})
    (False, 'restaurant', 200)
    """
    ########################
    # Start writing code
    ########################
    total_expense = 0

    for expense_name, expense_value in expenses.items():
        if expense_value > max_expense:
            RESULT = (False, expense_name, expense_value)
            ########################
            # End writing code
            ########################
            return RESULT
        total_expense += expense_value

    if total_expense <= monthly_budget:
        RESULT = (True, total_expense)
    else:
        RESULT = (False, total_expense)

    ########################
    # End writing code
    ########################
    return RESULT


def task3(input_value):
    """
    This function accepts one parameter returns either 'odd', 'even' or None.
    The function determines whether or not
        a) if the numerical value is odd or even
        b) if the number of characters of a string is odd or even
        c) if the number of elements in a list, set or tuple is add or even
        d) If any other data type, there is no return

    NOTE: you are required to add the neccessary paramaters, method body and return statement.
    NOTE: you are expected to determine the data type of the parameter and return the appropriate string value


    >>> task3("hello world")
    'odd'
    >>> task3(1234)
    'even'
    >>> task3({1,1,2,3,4,5,2,3,4,5,6})
    'even'
    >>> task3(list(range(2, 11)))
    'odd'
    >>> task3(tuple("cool"))
    'even'
    """
    ########################
    # Start writing code
    ########################
    if isinstance(input_value, int):
        RESULT = 'odd' if input_value % 2 != 0 else 'even'
    elif isinstance(input_value, str):
        RESULT = 'odd' if len(input_value) % 2 != 0 else 'even'
    elif isinstance(input_value, (list, set, tuple)):
        RESULT = 'odd' if len(input_value) % 2 != 0 else 'even'
    else:
        RESULT = None
    ########################
    # End writing code
    ########################
    return RESULT


# Example test cases
if _name_ == "_main_":
    # Task 1 tests
    print(task1(100000))
    print(task1(180000))
    print(task1(250000))
    print(task1('23456'))
    print(task1('55000'))

    # Task 2 tests
    print(task2(100, 40, {'food': 20, 'fun': 15, 'clothes': 30, 'travel': 25}))
    print(task2(150, 35, {'food': 30, 'books': 35, 'internet': 40, 'streaming services': 15}))
    print(task2(180, 40, {'food': 30, 'fun': 25, 'clothes': 30, 'travel': 25, 'books': 35, 'internet': 40,'streaming services': 15}))
    print(task2(300, 50,{'coat': 30, 'jeans': 20, 'hat': 15, 'scarf': 10, 'boots': 40, 'socks': 5, 'food': 20, 'fun': 15,'clothes': 30, 'travel': 25}))
    print(task2(500, 100, {'coffee': 40, 'restaurant': 200, 'travel': 50, 'plan ticket': 350,'school': 90}))

    # Task 3 tests
    print(task3("hello world"))
    print(task3(1234))
    print(task3({1, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6}))
    print(task3(list(range(2, 11))))
    print(task3(tuple("cool")))
