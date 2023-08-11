t = int(input())
for _ in range(t):
    n = int(input())

    ans = [0] * n
    if n == 1:
        print("1")
    elif n == 2:
        print("1 2")
    else:
        ans[0] = 2
        ans[n - 1] = 3
        mid = n // 2
        ans[mid] = 1
        id_ = 4
        for i in range(n):
            if i != 0 and i != n - 1 and i != mid:
                ans[i] = id_
                id_ += 1

        print(" ".join([str(x) for x in ans]))
