def find_outlier(integers):
    box_one = []
    box_two = []
    for _ in integers:
        if _ % 2 == 0:
            box_one.append(_)
        else:
            box_two.append(_)
    if len(box_one) == 1:
        return box_one[0]
    else:
        return box_two[0]