from collections import Counter

t = int(input())

for _ in range(t):
    s = input()
    if len(s) <= 1:
        print("NO")
    else:
        s = s[:len(s) // 2]
        if len(Counter(s)) >= 2:
            print("YES")
        else:
            print("NO")
