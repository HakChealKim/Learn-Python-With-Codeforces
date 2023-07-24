
t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    min_, max_ = min(lst), max(lst)
    if min_ < 0:
        print(min_)
    else:
        print(max_)


