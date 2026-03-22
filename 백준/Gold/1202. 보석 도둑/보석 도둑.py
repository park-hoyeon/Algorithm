import heapq
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
weight = []

for _ in range(n):
    m,v = map(int, input().split())
    heapq.heappush(weight, (m,v))

bags = []
for _ in range(k):
    c = int(input())
    bags.append(c)

bags.sort()

candidate = []
answer = 0

for c in bags:
    while weight and weight[0][0] <= c:
        m,v = heapq.heappop(weight)
        heapq.heappush(candidate, -v)

    if candidate:
        answer += -heapq.heappop(candidate)

print(answer)