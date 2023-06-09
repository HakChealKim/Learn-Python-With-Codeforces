import math


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    res = 0
    last = 0
    for i in range(1, n + 1, k):
        res += 1
        last = i
    if last < n:
        res += 1
    print(res)
