from math import inf

t = int(input())
for _ in range(t):
    n = int(input())
    pq = []
    sum_ = 0
    m1, m2 = inf, inf
    for _ in range(n):
        m = int(input())
        a = list(map(int, input().split()))
        a.sort()

        sum_ += a[1]
        m1 = min(m1, a[1])
        m2 = min(m2, a[0])

    sum_ += m2 - m1
    print(sum_)

#4
#5 7 1001 1007
#3
#6 8 11

#2
#2 9

#5 7 1001 1007
#2 9

