# student_module.py

def my_student_file(first_name, last_name):
    with open('Student_Number.txt', 'w') as file:
        file.write(f"{first_name}\n")
        file.write(f"{last_name}\n")

def student_info():
    student_number = input("Enter student number: ")
    first_name = input("Write your first name: ")
    last_name = input("Write your last name: ")
    my_student_file(first_name, last_name)

def main():
    student_info()

if __name__ == "__main__":
    main()
