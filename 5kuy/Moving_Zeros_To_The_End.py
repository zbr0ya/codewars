def move_zeros(lst):
    box = []
    box_one = []
    for _ in lst:
        if _ == 0:
            box.append(_)
        else:
            box_one.append(_)
    lst = box_one + box
    return lst