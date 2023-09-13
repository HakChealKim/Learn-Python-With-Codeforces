t = int(input())

for i in range(1, t):
    n = int(input())
    a = list(map(int, input().split()))

    b = {}

    for j in range(n):
        b[a[i]] = j + 1

    if b.keys() != b.values()[::-1]:
        print("NO")
    else:
        print("YES")


T = int(input())
for _ in range(0, T):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(0, n):
        d[a[i]] = i + 1
    if list(d.keys()) == list(d.values())[::-1]:
        print("YES")
    else:
        print("NO")