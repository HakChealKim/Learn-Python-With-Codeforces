t = int(input())
for _ in range(t):
    n = int(input())

    if n % 2 == 0:
        print("No")
    else:
        print("Yes")
        tot = 1 + 2 * n - n // 2
        for i in range(1, n + 1, 2):
            print(i, tot - i)
            tot += 1

        for i in range(2, n, 2):
            print(i, tot - i)
            tot += 1




