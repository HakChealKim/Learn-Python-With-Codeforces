n = int(input())

for _ in range(n):
    t = int(input())
    lst = list(map(int, input().split()))
    tot = sum(lst)

    ans = 0
    for v in lst:
        if v % 2 == 0:
            ans += v

    if ans > tot - ans:
        print('YES')
    else:
        print('NO')

