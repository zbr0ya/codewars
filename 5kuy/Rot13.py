import string


def rot13(message):
    rot_13 = 13
    send_box = []
    lower_box = list(string.ascii_lowercase * 2)
    upper_box = list(string.ascii_uppercase * 2)
    for _ in message:
        # print(_)
        if _.isalpha():
            if _.isupper() is False:
                if _ in lower_box:
                    # print(lower_box.index(_))
                    code_letter = lower_box.index(_) + 13
                    send_box.append(lower_box[code_letter])

            elif _.isupper() is True:
                if _ in upper_box:
                    upper_letter = upper_box.index(_) + 13
                    send_box.append(upper_box[upper_letter])
        else:
            send_box.append(_)

    return "".join(send_box)