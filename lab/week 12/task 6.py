import os


def search_student_number(student_number):
    file_name = f"{student_number}.txt"
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()

            first_name = lines[0].strip()
            last_name = lines[1].strip()
            print("Student found!")
            print(f"Student Number: {student_number}")
            print(f"First Name: {first_name}")
            print(f"Last Name: {last_name}")
    else:
        print("Sorry, student not found.")


def search_first_name(first_name):
    for file_name in os.listdir():
        if file_name.endswith(".txt"):
            with open(file_name, "r") as file:
                lines = file.readlines()
                if lines[0].strip().lower() == first_name.lower():
                    student_number = file_name.split(".")[0]
                    last_name = lines[1].strip()
                    print("Student found!")
                    print(f"Student Number: {student_number}")
                    print(f"First Name: {first_name}")
                    print(f"Last Name: {last_name}")
                    return
    print("Sorry, student not found.")


def search_last_name(last_name):
    for file_name in os.listdir():
        if file_name.endswith(".txt"):
            with open(file_name, "r") as file:
                lines = file.readlines()
                if lines[1].strip().lower() == last_name.lower():
                    student_number = file_name.split(".")[0]
                    first_name = lines[0].strip()
                    print("Student found!")
                    print(f"Student Number: {student_number}")
                    print(f"First Name: {first_name}")
                    print(f"Last Name: {last_name}")
                    return
    print("Sorry, student not found.")


def main():
    print("Search for a student by:")
    print("1. Student Number")
    print("2. First Name")
    print("3. Last Name")
    choice = input("Enter your choice: ")

    if choice == "1":
        student_number = input("Enter student number: ")
        search_student_number(student_number)
    elif choice == "2":
        first_name = input("Enter first name: ")
        search_first_name(first_name)
    elif choice == "3":
        last_name = input("Enter last name: ")
        search_last_name(last_name)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
