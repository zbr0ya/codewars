# def validator_first_arg(word: str):
#     if len(word) > 0:
#         return word
#     else:
#         return 0
#
# def str_count(strng="", letter="z"):
#     if len(validator_first_arg(strng)) > 0:
#         res = list(validator_first_arg(strng)).count(letter)
#         return int(res)
#     else:
#         return 0
#
#
# print(str_count())


def validator_first_arg(word: str):
    if len(word) > 0:
        return True
    else:
        return False


def str_count(strng="hello world", letter="o"):
    if validator_first_arg(strng) is True:
        res = list(strng).count(letter)
        return int(res)
    else:
        return 0


print(str_count())