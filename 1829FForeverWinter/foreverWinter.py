from collections import defaultdict

t = int(input())

for _ in range(t):

    n, m = map(int, input().split())

    g = defaultdict(list, [])
    degree = [0] * n

    for _ in range(m):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        g[a].append(b)
        g[b].append(a)
        degree[a] += 1
        degree[b] += 1

    k = 0

    for i in range(n):
        if degree[i] == 1:
            k += 1
    x = (n - 1) - k
    y = k // x

    print(str(x) + " " + str(y))
