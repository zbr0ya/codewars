def to_nato(words):
    #your code here
    encode_nato_words = {'a': 'Alfa',
                         'b': 'Bravo',
                         'c': 'Charlie',
                         'd': 'Delta',
                         'e': 'Echo',
                         'f': 'Foxtrot',
                         'g': 'Golf',
                         'h': 'Hotel',
                         'i': 'India',
                         'j': 'Juliett',
                         'k': 'Kilo',
                         'l': 'Lima',
                         'm': 'Mike',
                         'n': 'November',
                         'o': 'Oscar',
                         'p': 'Papa',
                         'q': 'Quebec',
                         'r': 'Romeo',
                         's': 'Sierra',
                         't': 'Tango',
                         'u': 'Uniform',
                         'v': 'Victor',
                         'w': 'Whiskey',
                         'x': 'Xray',
                         'y': 'Yankee',
                         'z': 'Zulu'}
    decode_box = []
    for _ in list(words.lower()):
        if _ in encode_nato_words:
            decode_box.append(encode_nato_words[_])
        elif _ == ' ':
            continue
        else:
            decode_box.append(_)
    return ' '.join(decode_box)