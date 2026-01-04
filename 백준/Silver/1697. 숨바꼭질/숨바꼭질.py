import sys
from collections import deque
input = sys.stdin.readline

MAX = 10**5

def bfs(n,k):
    dist = [-1] * (MAX+1)
    q = deque([n])
    dist[n] = 0

    while q:
        x = q.popleft()

        if x == k:
            return dist[x]

        for nx in (x-1, x+1, x*2):
            if 0<=nx<=MAX and dist[nx] == -1:
                dist[nx] = dist[x]+1
                q.append(nx)
n,k = map(int, input().split())
print(bfs(n,k))