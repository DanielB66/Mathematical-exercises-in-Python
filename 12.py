def pyramid(n: int):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j * i, end=' ')
        print()
    for i in range(n-1, 0, -1):
        for j in range(1, i+1):
            print(j * i, end=' ')
        print()

pyramid(7)