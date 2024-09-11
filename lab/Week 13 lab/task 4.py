# task4.py

import os

def new():
    new_folder = "new_directory"
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
        print(f"Directory '{new_folder}' created.")
    else:
        print(f"Directory '{new_folder}' already present.")

if __name__ == "__main__":
    new()
