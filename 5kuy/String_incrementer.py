def increment_string(strng):
    if strng.isalpha() or not strng or strng[-1].isalpha():
        return strng + '1'
    else:
        box_strng = []
        for _ in list(strng[::-1]):
            if _.isdigit():
                box_strng.append(_)
            else:
                break
    not_delete_box = list(strng[0:-len(box_strng)])
    number_box = ''.join(box_strng[::-1])
    sum_number = int(number_box) + 1
    total_number = str(sum_number).zfill(len(number_box))
    return f"{''.join(not_delete_box)}{total_number}"
