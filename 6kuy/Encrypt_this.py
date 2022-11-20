def encrypt_this(text):
    decode_text = list(text.split())
    send_box = []
    for _ in decode_text:
        # print(_)
        if len(_) >=3:
            send_box.append(f'{ord(_[0])}{_[-1]}{_[2:-1]}{_[1]}')
        elif len(_) == 1:
            send_box.append(str(ord(_)))
        else:
            send_box.append(f'{ord(_[0])}{_[1]}')
    return ' '.join(send_box)