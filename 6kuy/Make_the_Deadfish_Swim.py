def parse(data):
    # TODO: your code here
    send_dict = []
    validate_data = list(data)
    sum_i = 0
    for i in validate_data:
        if i == 'i':
            sum_i = sum_i + 1
        elif i == 's':
            sum_i = sum_i * sum_i
        elif i == 'd':
            sum_i = sum_i - 1
        elif i == 'o':
            send_dict.append(sum_i)


    return send_dict