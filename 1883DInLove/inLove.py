import heapq
from collections import defaultdict

q = int(input())

ldict, rdict = defaultdict(int), defaultdict(int)
pq_l = []
pq_r = []

for _ in range(q):
    op, l, r = map(str, input().split())
    l, r = int(l), int(r)
    if op == "+":
        ldict[l] += 1
        rdict[r] += 1
        heapq.heappush(pq_l, -l)
        heapq.heappush(pq_r, r)

    if op == "-":
        ldict[l] -= 1
        rdict[r] -= 1

    while len(pq_l) > 0 >= ldict[-pq_l[0]]:
        heapq.heappop(pq_l)
    while len(pq_r) > 0 >= rdict[pq_r[0]]:
        heapq.heappop(pq_r)

    if len(pq_l) > 0 and pq_r[0] < -pq_l[0]:
        print("Yes")
    else:
        print("No")


