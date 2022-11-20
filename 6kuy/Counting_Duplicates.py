def duplicate_count(text):
    # Your code goes here
    if len(text) <= 1:
        return 0
    else:
        box = []
        new_text = list(text.lower())
        for _ in new_text:
            if new_text.count(_) > 1:
                # box.append({_ :text.count(_)})
                box.append(_)
            else:
                continue
        return len(set(box))