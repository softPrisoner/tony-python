# character clear....
def clear_input():
    user_input = "This\nstring has \tsome whitespaces ... \r\n"

    # this match mapping
    character_mapping = {
        ord('\n'): ' ',
        ord('\t'): ' ',
        ord('\r'): None
    }
    clear_text = user_input.translate(character_mapping)
    print(clear_text)

if __name__ == "__main__":
    clear_input()
