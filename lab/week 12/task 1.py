# task 1.py

def file_list(filename, items):
    with open(filename, 'w') as file:
        for item in items:
            file.write(item + '\n')

if __name__ == "__main__":

    strings_list = ["Apple", "Pears", "Orange"]
    file_list('example.txt', strings_list)
