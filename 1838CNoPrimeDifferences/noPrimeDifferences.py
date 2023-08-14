from math import sqrt

t = int(input())


def is_prime(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


for _ in range(t):
    n, m = map(int, input().split())
    ans = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            ans[i][j] = m * i + j + 1

    if not is_prime(m):
        for k in range(n):
            print(*ans[k])
    else:
        if n == 4:
            print(*ans[2])
            print(*ans[0])
            print(*ans[3])
            print(*ans[1])
        else:
            for k in range(0, n, 2):
                print(*ans[k])
            for k in range(1, n, 2):
                print(*ans[k])
