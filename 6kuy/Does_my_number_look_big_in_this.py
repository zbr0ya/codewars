def narcissistic( value ):
    # Code away
    box = []
    # print(list(str(value)))
    for _ in list(str(value)):
        box.append(int(_) ** len(str(value)))
    # return sum(box)
    if sum(box) == value:
        return True
    else:
        return False