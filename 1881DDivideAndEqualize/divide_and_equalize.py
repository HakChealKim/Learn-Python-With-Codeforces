from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = Counter()
    for c in a:
        i = 2

        while i <= c // i:
            while c % i == 0:
                cnt[i] += 1
                c //= i
            i += 1
        if c > 1:
            cnt[c] += 1
    tag = True
    for _, v in cnt.items():
        if v % n:
            print("No")
            tag = False
            break

    if tag:
        print("Yes")



#5
#100 2 50 10 1

# 100 -> 2 2 5 5 1
# 2 -> 2 1
# 50 -> 2 5 5 1
# 10 -> 2 5 1
# 1  -> 1