import math

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    d, ret = 0, 0
    for i in range(1, len(a)):
        d = max(0, math.ceil(math.log2(a[i - 1] / a[i])) + d)
        ret += d
    print(ret)

