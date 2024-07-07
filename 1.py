def mystery(numbers: list) -> list:
    list1 = []
    for num in range(1,11):
        if num not in numbers:
            list1.append(num)
    return list1

print(mystery([1,2,4,8]))
