

t = int(input())

for _ in range(t):
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))

    tot = 0

    dp = [0] * (n + 1)

    for i in range(len(a) - 1, -1, -1):
        if a[i] <= q:
            dp[i] = dp[i + 1] + 1

    for i in range(len(a) - k + 1):

        status = True
        for j in range(i, i + k):
            if a[j] > q:
                status = False

        if status:
            tot += dp[i + k - 1]

    print(tot)
