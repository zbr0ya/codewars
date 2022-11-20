def spin_words(sentence):
    # Your code goes here
    send_box = [x if len(x) < 5 else x[::-1] for x in list(sentence.split())]
    return ' '.join(send_box)