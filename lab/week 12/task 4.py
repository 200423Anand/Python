# task4.py
import csv

def read_my_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['Username']: <10} {row['First Name']: <12} {row['Last Name']: <12} {row['Age']}")

if __name__ == "__main__":
    read_my_csv('data.csv')
