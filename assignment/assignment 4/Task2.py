import os

path = input("Enter a path that you want to open: ")

if not os.path.exists(path):
    raise Exception("Path does not exist in the system.")

total_files_and_folders = 0
total_files = 0
total_folders = 0

for root, dirs, files in os.walk(path):
    total_files_and_folders += len(dirs) + len(files)
    total_files += len(files)
    total_folders += len(dirs)

print(f"{total_files_and_folders} files and folders.")
print(f"{total_folders} folder(s).")
print(f"{total_files} file(s).")
