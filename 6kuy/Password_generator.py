import pprint
import random
import string


"""функція для генерування 3 рандомних чісел з їх максимальною сумою 20 і мінімальною 6 для коректної валідації вказаної в завданні"""
def new_foo():
    box = []
    box_number = []
    for _ in range(1, 10):
        box.append(_)

    for _ in range(1, 4):
        number = random.choice(box)
        box_number.append(number)
    if sum(box_number) >= 6 and sum(box_number) <= 20:
        return box_number
    else:
        return new_foo()


"""функція задана на codewars"""
def password_gen():
    validator_len = new_foo()

    """створяємо списки для всіх груп"""
    pasword_number_box = []
    box_lower_letter = []
    box_UPPER_letter = []

    """генеруємо рандомну кількість чісел"""
    posible_number = ['0','1','2','3','4','5','6','7','8','9']
    for _ in range(validator_len[0]):
        pasword_number_box.append(random.choice(posible_number))

    # print(pasword_number_box)
    """генеруємо рандомну кількість малих букв"""
    for i in range(validator_len[1]):
        box_lower_letter.append(random.choice(list(string.ascii_lowercase)))
    # print(box_lower_letter)

    """генеруємо рандомну кількість ВЕЛИКИХ букв"""
    for i in range(validator_len[2]):
        box_UPPER_letter.append(random.choice(list(string.ascii_uppercase)))
    # print(box_UPPER_letter)

    """створюємо загальний список"""
    total_pasword_info = []
    total_pasword_info = pasword_number_box + box_lower_letter + box_UPPER_letter

    """змішуємо все"""
    random.shuffle(total_pasword_info)
    # print(total_pasword_info)

    """і відправляємо"""
    send_password = "".join(total_pasword_info)
    return send_password

