t = int(input())
for _ in range(t):
    n, m, h = map(int, input().split())
    tt = list()

    for i in range(n):
        lst = list(map(int, input().split()))
        lst.sort()
        tot_times, point, penalty = 0, 0, 0

        for j in range(len(lst)):
            tot_times += lst[j]
            if tot_times <= h:
                point += 1
                penalty += tot_times
                if j == len(lst) - 1:
                    tt.append((point, penalty, i))
            else:
                tt.append((point, penalty, i))
                break

    tt.sort(key=lambda x: (-x[0], x[1]))

    for i in range(len(tt)):
        if tt[i][2] == 0:
            print(i + 1)
