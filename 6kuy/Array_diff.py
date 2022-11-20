def array_diff(a, b):
    #your code here
    if not a:
        return a
    else:
        send_box = []
        for _ in a:
            if _ in b:
                continue
            else:
                send_box.append(_)
    return send_box