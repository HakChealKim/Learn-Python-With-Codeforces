t = int(input())


for i in range(t):

    a, b, c, d = map(int, input().split())
    if d >= b and c <= a + d - b:
        print(d - b + a + d - b - c)
    else:
        print(-1)


