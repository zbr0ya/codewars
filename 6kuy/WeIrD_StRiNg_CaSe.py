def to_weird_case(words):
    count = 0
    box = []
    for _ in words:
        if _.isalpha():
            count = count + 1
            if count % 2 != 0:
                box.append(_.upper())
            else:
                box.append(_.lower())
        else:
            _ == ' '
            box.append(' ')
            count = 0

    return ''.join(box)