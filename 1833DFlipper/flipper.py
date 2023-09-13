for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(*a)
        continue

    i = a.index(n - 1 if a[0] == n else n)
    if i == n - 1:
        i = n

    j = i - 2
    while j > 0 and a[j] > a[0]:
        j -= 1
    print(*(a[i:] + a[j + 1:i][::-1] + a[:j + 1]))


