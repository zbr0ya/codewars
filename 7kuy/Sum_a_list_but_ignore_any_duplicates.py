def sum_no_duplicates(l):
    # write your solution here
    l2 = [n for n in l if int(l.count(n)) == 1]
    return sum(l2)