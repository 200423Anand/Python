# task 2.py

def file_read(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    file_read('example.txt')
