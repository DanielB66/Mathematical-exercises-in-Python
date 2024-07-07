word = input('Enter a word: ')
for i in range(len(word)):
    for x in range(i+1):
        print(word[x], end='')
    print()
