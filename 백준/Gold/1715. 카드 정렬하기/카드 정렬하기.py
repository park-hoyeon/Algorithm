import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []

for _ in range(n):
    heapq.heappush(heap, int(input()))

store = []

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    new = a + b
    store.append(new)
    heapq.heappush(heap, new)

print(sum(store))