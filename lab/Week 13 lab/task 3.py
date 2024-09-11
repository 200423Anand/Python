# task3.py

import os

def main():
    directories_and_files = os.listdir()
    for item in directories_and_files:
        print(item)

if __name__ == "__main__":
    main()
