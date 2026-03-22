import heapq
import sys
input = sys.stdin.readline

n = int(input())

left = []
right = []

for _ in range(n):
    data = int(input())

    if len(left) == len(right):
        heapq.heappush(left, -data)
    else:
        heapq.heappush(right, data)

    if right and -left[0] > right[0]:
        l = -heapq.heappop(left)
        r = heapq.heappop(right)

        heapq.heappush(left, -r)
        heapq.heappush(right, l)

    print(-left[0])