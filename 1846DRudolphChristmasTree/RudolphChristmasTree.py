t = int(input())
for _ in range(t):
    n, d, h = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()

    tot = n * d * h / 2
    pre = lst[0]

    for i in range(1, len(lst)):
        if pre + h > lst[i]:
            hh = h - lst[i] + pre
            dd = d * hh / h
            tot -= hh * dd / 2

        pre = lst[i]

    print(tot)




