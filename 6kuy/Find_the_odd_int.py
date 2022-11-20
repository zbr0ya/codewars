def find_it(seq):
    if len(seq) == 1:
        return seq[0]
    else:
        for _ in list(seq):
            if seq.count(_) % 2 == 1:
                return _
            else:
                continue
