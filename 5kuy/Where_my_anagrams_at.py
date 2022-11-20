def anagrams(word, words):
    # your code here
    validate_box = [w for w in words if len(w) == len(word)]
    if not validate_box:
        return validate_box
    else:
        send_box = []
        sort_word = ''.join(sorted(list(word)))
        for _ in validate_box:
            if ''.join(sorted(list(_))) == sort_word:
                send_box.append(_)
            else:
                continue

        return send_box
