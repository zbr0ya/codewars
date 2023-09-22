def positive_sum(arr):
    # Your code here
    # res = (x for x in arr if x > 0)
    # print(sum(res))
    print(sum(x for x in arr if x > 0))
    return sum(x for x in arr if x > 0)
    # if len(arr) == 0:
    #     print(0)
    #     return 0
    # else:
    #     print(sum(arr))
    #     return sum(arr)



positive_sum([1,-2,3,4,5])
