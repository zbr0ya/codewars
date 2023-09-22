def opposite(number):
  # your solution here
    if number < 0:
        print(abs(-number))
        return abs(-number)
    else:
        print(-abs(number))
        return -abs(number)


opposite(1)