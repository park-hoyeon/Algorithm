import sys
input = sys.stdin.readline
import heapq

heap= []
n = int(input())

for _ in range(n):
    data = int(input())

    if data != 0:
        heapq.heappush(heap, (abs(data), data))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)