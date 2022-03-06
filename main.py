from morse_code import morse_code_dict


def convert_text_to_morse_code(text):
    morse_code_conversion = ""
    for character in text:
        morse_code_conversion = morse_code_conversion + morse_code_dict[character]
    return morse_code_conversion


def user_text():
    return input("Enter text to convert into morse code:\n> ").lower()


def main():
    text = user_text()
    morse_code = convert_text_to_morse_code(text)
    print(morse_code)


if __name__ == "__main__":
    main()
