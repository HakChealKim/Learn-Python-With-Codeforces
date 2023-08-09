t = int(input())
for _ in range(t):
    x = input()
    x = '0' + x
    letter = [v for v in x]

    n = len(letter)
    i = n - 1
    p = -1
    while i > 0:
        if letter[i] >= '5':
            letter[i - 1] = chr(ord(letter[i - 1]) + 1)
            p = i
        i -= 1
    if p != -1:
        for k in range(p, n):
            letter[k] = '0'

    print(int("".join(letter)))
