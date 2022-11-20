def count_bits(n):
    bite = bin(n)
    box = []
    for _ in bite[2:]:
        if int(_) == 1:
            box.append(_)
    return len(box)