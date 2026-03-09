import sys
input = sys.stdin.readline
import heapq

n,m = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
heap = []

for i in range(min(m,n)):
    heapq.heappush(heap, data[i])

for i in range(m,n):
    a = heapq.heappop(heap)
    new = a + data[i]
    heapq.heappush(heap, new)

print(max(heap))