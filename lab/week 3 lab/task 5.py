year = int(input("Please enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Yes, {year} is a leap year.")
        else:
            print(f"No, {year} is not a leap year.")
    else:
        print(f"Yes, {year} is a leap year.")
else:
    print(f"No, {year} is not a leap year.")
