def count_character(input_string):
    char_frequency = {}

    for char in input_string:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    print("Character frequency:")
    for char, freq in char_frequency.items():
        print(f"{char}: {freq}")

input1 = input("Enter a string: ")
count_character(input1)