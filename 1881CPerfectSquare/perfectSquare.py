t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        s = input()
        arr.append(s)

    ret = 0
    for i in range(n // 2):
        for j in range(n // 2):
            a, b, c, d = arr[i][j], arr[j][n - i - 1], arr[n - i - 1][n - j - 1], arr[n - j - 1][i]
            f = max(ord(a), ord(b), ord(c), ord(d))
            ret += 4 * f - ord(a) - ord(b) - ord(c) - ord(d)
    print(ret)
