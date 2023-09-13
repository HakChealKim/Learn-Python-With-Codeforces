import math

t = int(input())

def lcm(x, y):
    return x * y // math.gcd(x, y)


for i in range(t):
    n, x, y = map(int, input().split())
    m = lcm(x, y)
    c1, c2 = n // x - n // m, n // y - n // m
    diff = c1 * (n - c1 + 1 + n) // 2 - c2 * (1 + c2) // 2
    print(diff)


