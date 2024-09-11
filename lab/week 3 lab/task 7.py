letter = input("Please enter a letter: ").lower()

if letter in 'a e i o u':
    print(f"The letter '{letter}' is a vowel.")
    if letter == 'a':
        print("It is the vowel 'a'.")
    elif letter == 'e':
        print("It is the vowel 'e'.")
    elif letter == 'i':
        print("It is the vowel 'i'.")
    elif letter == 'o':
        print("It is the vowel 'o'.")
    elif letter == 'u':
        print("It is the vowel 'u'.")
else:
    print(f"The letter '{letter}' is not a vowel.")
