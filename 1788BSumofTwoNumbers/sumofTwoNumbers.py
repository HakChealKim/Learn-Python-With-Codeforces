t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    id_1, id_2, id_n = -1, -1, -1

    for i in range(len(p)):
        if p[i] == 1:
            id_1 = i
        if p[i] == 2:
            id_2 = i
        if p[i] == n:
            id_n = i

    id_x1, id_x2 = min(id_1, id_2) + 1, max(id_1, id_2) + 1
    id_1, id_2 = id_x1, id_x2
    id_n += 1

    if id_1 <= id_n <= id_2:
        print(id_n, id_n)
    elif id_n <= id_1:
        print(id_n, id_1)
    else:
        print(id_2, id_n)
