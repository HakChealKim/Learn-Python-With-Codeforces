t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    h = list(map(int, input().split()))

    l, r = 0, 0
    pre = 0
    f = 0
    ans = 0
    while r < n:
        if r == 0 or h[r - 1] % h[r] == 0:
            f += a[r]
            r += 1
        else:
            f = a[r]
            l = r
            r += 1

        while l <= r and f > k:
            f -= a[l]
            l += 1

        ans = max(ans, r - l)
    print(ans)
