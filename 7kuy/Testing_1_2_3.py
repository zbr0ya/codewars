def number(lines):
    send_box = []
    for num, word in enumerate(lines, 1):
        send_box.append(f"{num}: {word}")
    return send_box