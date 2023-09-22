t = int(input())

for _ in range(t):
    s = input()
    ans = 0
    i = 0
    ans = 0
    arr = s.split("B")
    arr.sort()
    for i in range(1, len(arr)):
        ans += len(arr[i])
    print(ans)
