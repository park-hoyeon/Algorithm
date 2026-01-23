import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int, input().split())
MAX = 100000
road = [-1] * (MAX + 1)

queue = deque()
queue.append(n)
road[n] = 1

while queue:
    popN = queue.popleft()
    if popN == k:
        print(road[k]-1)
        break
    for newN in (2*popN, popN-1, popN+1):
        if not (0<=newN<=MAX):
            continue

        if road[newN] != -1:
            continue

        if newN == 2 * popN:
            road[newN] = road[popN]
            queue.appendleft(newN)
        else:
            road[newN] = road[popN] + 1
            queue.append(newN)