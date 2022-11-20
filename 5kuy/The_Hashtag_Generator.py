def generate_hashtag(s):
    #your code here
    if len(s) == 0 or len(s) > 140:
        return False
    else:
        send_hashtag = [h.title() for h in list(s.split())]
        return f"#{''.join(send_hashtag)}"
        print(send_hashtag)