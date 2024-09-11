user_input = input("Enter your string: ")

search_char = input("Enter a character that you want to search for: ")

is_char_found = search_char in user_input

print("Character found:", is_char_found)

if is_char_found:
    first_position = user_input.find(search_char)
    print("First word of the character:", first_position)
