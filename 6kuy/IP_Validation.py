def is_valid_IP(strng):
    if not strng or len(strng) < 7:
        return False
    else:
        send_box = []
        validate_ip = strng.split('.')
        for _ in validate_ip:
            if _.isdigit() is True:
                if int(_) >= 0 and int(_) <= 255:
                    send_box.append(_)
                else:
                    return False
            else:
                return False
    res_box = []
    for _ in send_box:
        if _[0] == '0' and len(_) >= 2:
            return False
        else:
            res_box.append(_)
    if len(res_box) == 4:
        return True
    else:
        return False