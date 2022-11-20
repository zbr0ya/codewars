import string

def alphabet_position(text):
    number_alphabet_position = list(string.ascii_lowercase)
    box_send = []
    for _ in text.lower():
        if _.isalpha():
            index = number_alphabet_position.index(_)
            box_send.append(str(index + 1))
        else:
            continue
    return ' '.join(box_send)