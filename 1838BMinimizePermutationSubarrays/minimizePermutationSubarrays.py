t = int(input())
for _ in range(t):
    n = int(input())

    s1, s2 = [], []

    revert = False

    while n:
        x = n % 10
        n //= 10
        x1, x2 = x // 2, x - x // 2
        if x1 != x2:
            revert = not revert

        if revert:
            s1.append(str(x//2))
            s2.append(str(x - x // 2))
        else:
            s2.append(str(x//2))
            s1.append(str(x - x // 2))

    s1.reverse()
    s2.reverse()
    print(int("".join(s1)), int("".join(s2)))
