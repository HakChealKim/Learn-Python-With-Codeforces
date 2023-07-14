t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    if x == 1:
        if k == 1:
            print("NO")
        elif k == 2:
            if n % 2 == 0:
                print("YES")
                print(n // 2)
                print("2 " * (n // 2))
            else:
                print("NO")
        else:
            if n % 2 == 0:
                print("YES")
                print(n // 2)
                print("2 " * (n // 2))
            else:
                print("YES")
                n -= 3
                tot = 1
                tot += n // 2
                print(tot)
                print("3 " + "2 " * (tot - 1))
    else:
        print("YES")
        print(n)
        print("1 " * n)
