t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    pos, neg = 0, 0
    for x in lst:
        if x > 0:
            pos += 1
        else:
            neg += 1

    minlst = []
    for x in range(neg):
        minlst.append(1)
        minlst.append(0)
    v = 1
    for x in range(pos - neg):
        minlst.append(v)
        v += 1

    maxlst = []
    v2 = 1
    for x in range(pos):
        maxlst.append(v2)
        v2 += 1

    v2 -= 2
    for x in range(neg):
        maxlst.append(v2)
        v2 -= 1

    print(*maxlst)
    print(*minlst)