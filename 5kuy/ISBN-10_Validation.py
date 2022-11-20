def valid_ISBN10(isbn):
    # your code here
    if isbn.isdigit():
        validate_isbn = list(isbn)
    elif isbn[0:-1].isdigit() and isbn[-1] == 'X':
        validate_isbn = [v for v in isbn[0:-1]]
        validate_isbn.append('10')
    else:
        return False
    if len(validate_isbn) == 10:
        total_box = []
        integer_isbn = [int(i) for i in list(validate_isbn)]
        count_integer_isbn = [c for c in enumerate(integer_isbn, 1)]
        for _ in count_integer_isbn:
            total_box.append(_[0] * _[1])
        if sum(total_box) % 11 == 0:
            return True
        else:
            return False
    else:
        return False