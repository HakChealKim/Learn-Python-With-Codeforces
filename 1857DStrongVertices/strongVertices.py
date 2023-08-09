
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    res = []
    for i in range(n):
        res.append((a[i] - b[i], i + 1))

    res.sort(reverse=True)
    ans = []

    pre = res[0][0]
    ans.append(res[0][1])
    for i in range(1, len(res)):
        if res[i][0] >= pre:
            ans.append(res[i][1])
        else:
            break
    ans.reverse()
    print(len(ans))
    print(*ans)

