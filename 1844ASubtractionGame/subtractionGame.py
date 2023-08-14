t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    if a == 1:
        print(b + 1)
    else:
        print(a - 1)
