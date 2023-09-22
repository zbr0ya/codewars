def make_negative(number):
    # print(number - (number + 1))
    if number == 0 or number < 0:
        print(number)
        return number
    else:
        print(number - (2 * number))
        return number - (2 * number)


make_negative(1)