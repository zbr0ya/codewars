def domain_name(url):
    delete_this = [':', '/', '.']
    phh = ['www', 'org', 'co', 'biz', 'tv', 'it', 'pro', 'https', 'com', 'ru', 'http', 'jp']
    box = list(url)
    send_box = []
    domain_box = []
    for _ in box:
        if _ in delete_this:
            send_box.append(' ')
        else:
            send_box.append(_)
    total_url = list(''.join(send_box).split())
    for _ in total_url:
        if _ in phh:
            continue
        else:
            domain_box.append(_)
    return domain_box[0]