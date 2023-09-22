def count_sheeps(sheep):
    # sheeps = 0
    # for _ in sheep:
    #     if _ is True:
    #         sheeps += 1
    #     else:
    #         continue
    #
    # print(sheeps)
    return (x for x in sheep if x)



count_sheeps([False ])