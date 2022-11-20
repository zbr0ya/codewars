# return masked string
def maskify(cc):
    if len (cc) <= 4:
        return cc
    else:
        code_info =  list(cc[:-4])
        return len(code_info) * '#' + (cc[-4:-1]) + (cc[-1])