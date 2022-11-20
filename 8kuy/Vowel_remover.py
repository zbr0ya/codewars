def shortcut(s):
    del_this = ['a', 'e', 'i', 'o', 'u']
    return ''.join([x for x in s if x not in del_this])


"""or"""

# def shortcut(s):
#     del_this = ['a', 'e', 'i', 'o', 'u']
#     send_box = []
#     for _ in s:
#         if _ in del_this:
#             continue
#         else:
#             send_box.append(_)
#     return ''.join(send_box)