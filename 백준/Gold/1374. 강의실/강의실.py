import heapq
import sys
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    num,start,end = map(int, input().split())
    classes.append((start,end))
classes.sort()

candidate = []
heapq.heappush(candidate, classes[0][1])

for i in range(1, n):
    start = classes[i][0]
    end = classes[i][1]

    if candidate[0] <= start:
        heapq.heappop(candidate)

    heapq.heappush(candidate, end)

print(len(candidate))