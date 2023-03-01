def disemvowel(string_="This website is for losers LOL!"):
    # dell_letters = 'AEIOUaeiou'
    # """дерев'яний варіант"""
    # send_this = []
    # for _ in string_:
    #     if _ not in dell_letters:
    #         send_this.append(_)
    #     else:
    #         continue
    # return ''.join(send_this)
    # """трошки подумаю"""
    # info = [x for x in string_ if x not in 'AEIOUaeiou']
    # return ''.join(info)
    """пьорфект :)"""
    # info = [x for x in string_ if x not in 'AEIOUaeiou']
    return ''.join(x for x in string_ if x not in 'AEIOUaeiou')


print(disemvowel())