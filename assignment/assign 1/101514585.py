"""
Assignment 1 File

Full Nmae: Jatin_Sethi
Student_Number: 101514585

Only edit the text where indicated
Make sure that the final result of the function is stored in the variable RESULT
"""


def task1(text1, text2, text3):
    """
    returns the text that is the longest. if there is a tie, concatenate the text(s), seperated by underscores in same order of the arguments


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
    #######################
text1 = input("Enter text1:")
text2 = input("Enter text2:")
text3 = input("Enter text3:")

lengths = [len(text1), len(text2), len(text3)]

max_length = max(lengths)

if lengths.count(max_length) > 1:
    longest_texts = '_'.join([text for text, length in zip([text1, text2, text3], lengths) if length == max_length])
else:
    longest_texts = [text1, text2, text3][lengths.index(max_length)]
Final_ans = longest_texts

    ########################
    # End writing code
    ########################
print(Final_ans)


def task2(operand1, operator, operand2):
    """
    returns the result or an arithmetic operation. Accept the following four operators +, -, * & /.

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
    result = ''
    ########################
    # Start writing code
    ########################
operand1 = int(input("Enter operand1:"))
operator = input("Enter Operator:")
operand2 = int(input("Enter operand2:"))

if operator == "+":
    result = operand1 + operand2
elif operator == "-":
    result = operand1 - operand2
elif operator == "*":
    result = operand1 * operand2
elif operator == "/":
    if operand2 != 0:
        result = operand1 / operand2
    else:
        print("Error: Division by zero!")
else:
    print("Error: Invalid operator!")

print("Result is:",result)



    ########################
    # End writing code
    ########################



def task3(name):
    """
    Determines if name is valid. A valid name contains only one space and at least 5 characters
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
    result = ''
    ########################
    # Start writing code
    ########################
name = input("Enter name:")
if  len(name) == 5 and name.count(" ") == 0 or name.count(" ") == 1 :
    print(True)
else:
    print(False)

    ########################
    # End writing code
    ########################
   # return result


def task4(value, multiplier):
    """
    returns either a string repeated X times or the product of two numbers (the arithmetic operation). Return False if second argument is NOT a number
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
    result = ''
    ########################
    # Start writing code
    ########################
value = input("Enter anything:")
multiplier = int(input("Enter multiplier:"))

if not isinstance(multiplier, (int, float)):
    print(False)
else:
    try:
        value_str = str(value)
        result_str = value_str * int(multiplier)
        print(result_str)
    except ValueError:
        try:
            value_int = int(value)
            result_int = value_int * int(multiplier)
            print(result_int)
        except ValueError:
             print(False)
    ########################
    # End writing code
    ########################
    #return result

