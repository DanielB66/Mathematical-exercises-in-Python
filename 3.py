def mystery(numbers: list, dividers: list) -> list:
    newlist = []
    for x in numbers:
        isdivided = True
        for y in dividers:
            if x % y != 0:
                isdivided = False
                break
        if isdivided == True:
            newlist.append(x)
    return newlist


print(mystery([2, 3, 5, 6, 8, 9, 12, 14, 18, 20, 40], [2, 3]))
