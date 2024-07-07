num = int(input('enter a number: '))
x = 1
line = 1
while num >= x:
    for j in range(line):
        print(x, end='')
        x = x+1
        if x > num:
            break
    print()
    line = line + 1
