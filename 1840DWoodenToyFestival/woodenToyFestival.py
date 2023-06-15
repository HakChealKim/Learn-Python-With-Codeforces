

t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()


    def valid(d: int) -> bool:
        cnt = 0
        delta = lst[0] + d
        for v in lst:
            dis = abs(v - delta)
            if dis > d:
                cnt += 1
                delta = v + d

        return cnt < 3

    left, right = 0, lst[len(lst) - 1] - lst[0]

    while left < right:
        mid = (left + right) // 2

        if valid(mid):
            right = mid
        else:
            left = mid + 1

    print(left)