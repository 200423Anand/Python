# task5.py

import os

def create_directories():
    os.makedirs("d1/d2/d3", exist_ok=True)

def CreateTextFiles():
    dirs = ["d1", "d1/d2", "d1/d2/d3"]
    file_count = 1
    for dir in dirs:
        for i in range(2):
            FileName = f"{dir}/file{file_count}.txt"
            with open(FileName, 'w') as f:
                pass
            file_count += 1

def main():
    create_directories()
    CreateTextFiles()
    print("Your directories and Text files are created .")

if __name__ == "__main__":
    main()
