# task6.py

def main():
    try:
        user_input = input("Please enter a number of yours  choice : ")
        number = float(user_input)
        print("You entered:", number)
    except ValueError:
        import sys
        print("Error: Invalid number", file=sys.stderr)
    finally:
        print("Thank you for your respnse.")

if __name__ == "__main__":
    main()
