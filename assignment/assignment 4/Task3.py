numbers = [
    67, 18, 6, 68, 57,
    31, 61, 7, 59, 69,
    21, 92, 53, 43, 59,
    1, 4, 8, 13, 57
]

with open('below_50.txt', 'w') as below_file, open('above_50.txt', 'w') as above_file:
    for number in numbers:
        if 1 <= number <= 50:
            below_file.write(f"{number}\n")
        elif 51 <= number <= 100:
            above_file.write(f"{number}\n")

print("Numbers categorized and written to files successfully.")

