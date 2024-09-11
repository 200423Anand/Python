# task8.py

def main():
    FileName = input("Enter the name of your text file to open: ")

    if not FileName.endswith(".txt"):
        print("Error: File name should be end with .txt'")
        return

    try:
        with open(FileName, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: File not found")


if __name__ == "__main__":
    main()
