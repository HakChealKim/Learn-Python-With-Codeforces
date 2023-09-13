t = int(input())
a = [0] + list(map(int, input().split())) + [0]
ans = 0
for i in range(1, t + 1):
    if a[i - 1] != 0:
        a[i - 1] -= 1
    elif a[i] == 0 and a[i + 1] != 0:
        a[i + 1] -= 1
    else:
        ans += 1
print(ans)
