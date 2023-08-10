t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print("a")

    else:
        x = 2

        for i in range(2, n):
            if n % i != 0:
                x = i
                break

        ans = []

        for i in range(n):
            ch = chr(ord('a') + i % x)
            ans.append(ch)

        print("".join(ans))
