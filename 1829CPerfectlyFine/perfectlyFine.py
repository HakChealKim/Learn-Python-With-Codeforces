t = int(input())

for _ in range(t):
    n = int(input())
    a11, a01, a10 = 0, 0, 0
    for _ in range(n):
        m, s = input().split()
        m = int(m)

        if s == '11':
            if a11 == 0 or a11 > m:
                a11 = m
        elif s == '01':
            if a01 == 0 or a01 > m:
                a01 = m
        elif s == '10':
            if a10 == 0 or a10 > m:
                a10 = m

    if a11 == 0:
        if a01 == 0 or a10 == 0:
            print(-1)
        else:
            print(a01 + a10)
    else:
        if a01 == 0 or a10 == 0:
            print(a11)
        else:
            print(min(a11, a01 + a10))
