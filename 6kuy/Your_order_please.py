def order(sentence):
  # code here
    finde_order = list(sentence.split())
    dict_box = {}
    for _ in finde_order:
        for i in _:
            if i.isdigit():
                dict_box.update({int(i): _})
            else:
                continue
    send_box = []
    res = sorted(dict_box.items())
    for _ in res:
        send_box.append(_[1])
    return ' '.join(send_box)

"""or"""

# def order(sentence):
#   # code here
#     finde_order = list(sentence.split())
#     index_sentence = [x * '' for x in range(len(finde_order))]
#     dict_box = {}
#     for _ in finde_order:
#         for i in _:
#             if i.isdigit():
#                 dict_box.update({int(i): _})
#             else:
#                 continue
#     send_box = []
#     res = sorted(dict_box.items())
#     for _ in res:
#         send_box.append(_[1])
#     return ' '.join(send_box)