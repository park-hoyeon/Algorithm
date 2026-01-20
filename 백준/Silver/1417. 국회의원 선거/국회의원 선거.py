import sys
input = sys.stdin.readline
import heapq

heap = []
n = int(input())
dasom = int(input())

if n == 1:
    print(0)
    sys.exit()

for _ in range(n-1):
    x = int(input())
    heapq.heappush(heap,-x)

count = 0

while True:
    top = -heap[0]

    if dasom > top:
        break
    heapq.heappop(heap)
    top-=1
    dasom+=1
    count+=1
    heapq.heappush(heap, -top)
print(count)