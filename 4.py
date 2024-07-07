def mystery(x: int) -> int:
    z = 0
    while x != 0:
        y = x % 10
        x = x // 10
        z = z + y
    return z


print(mystery(124))
