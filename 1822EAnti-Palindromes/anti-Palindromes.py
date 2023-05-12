t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    if n % 2 == 1:
        print(-1)
        continue
    cnt = [0] * 26
    for v in s:
        cnt[ord(v) - 97] += 1

    if max(cnt) > n // 2:
        print(-1)
        continue

    cnt = [0] * 26
    ans = 0

    for i in range(n // 2):
        if s[i] == s[n - i - 1]:
           ans += 1
           cnt[ord(s[i]) - 97] += 1

    print(max(max(cnt), (ans + 1) // 2))
