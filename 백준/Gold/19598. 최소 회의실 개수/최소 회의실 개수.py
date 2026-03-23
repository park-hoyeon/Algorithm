import heapq
import sys
input = sys.stdin.readline

n = int(input())
room = []

for _ in range(n):
    a,b = map(int, input().split())
    room.append((a,b))

room.sort()

candidate = []
heapq.heappush(candidate, room[0][1])

for i in range(1,n):
    start, end = room[i]

    if candidate[0] <= start:
        heapq.heappop(candidate)

    heapq.heappush(candidate, end)

print(len(candidate))