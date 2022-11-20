def create_phone_number(n):
    #your code here
    new_n = []
    for _ in n:
        new_n.append(str(_))
    number_info = ''.join(new_n)
    send = f"({number_info[0:3]}) {number_info[3:6]}-{number_info[6:]}"
    print(send)
    return send