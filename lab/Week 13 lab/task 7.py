# task7.py

def main():
    try:
        user_input = input("Please enter an odd number: ")
        number = int(user_input)
        if number % 2 == 1:
            print("You entered an odd number:", number)
        else:
            import sys
            print("Error: This is  not a odd number ", file=sys.stderr)
    except ValueError:
        import sys
        print("Error: Invalid number", file=sys.stderr)

if __name__ == "__main__":
    main()
