t = int(input())
for _ in range(t):

    n = int(input())
    lst = list(map(int, input().split()))

    ans = [0] * n
    ans[n - 1] = lst[n - 2]
    ans[0] = lst[0]

    for i in range(n - 3, -1, -1):
        if lst[i] <= lst[i + 1]:
            ans[i + 1] = lst[i]
        else:
            ans[i + 1] = lst[i + 1]

    print(*ans)







