import os

filename = input("Enter a filename that you want to make: ")

if '.' not in filename:
    filename += '.txt'

if os.path.exists(filename):
    raise Exception("File already exists in the system!")

with open(filename, 'w') as file:
    pass

content = input("Enter content (at least 10 characters): ")

if len(content) < 10:
    raise Exception("Content must be at least 10 characters long.")

with open(filename, 'a') as file:
    file.write(content + '\n')

print("File created and content added successfully in the directory.")
