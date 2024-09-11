# task 3.py
import csv

def csv_file(filename, rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'First Name', 'Last Name', 'Age'])
        writer.writerows(rows)

if __name__ == "__main__":

    rows = [
        ['user1', 'Anand', 'Sharma', 19],
        ['user2', 'Sukhdeep', 'Kaur', 20],
        ['user3', 'Jatin', 'Sethi', 21]
    ]
    csv_file('data.csv', rows)
