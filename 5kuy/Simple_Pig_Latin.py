def pig_it(text):
    box = []
    for _ in list(text.split(' ')):
        if _.isalpha():
            info = _[1:] + _[0] + 'ay'
            box.append(info)
        else:
            box.append(_)
    return ' '.join(box)