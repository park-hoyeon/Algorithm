import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

def bfs(x,y,visited,blind):
    q = deque()
    q.append((x,y))
    visited[y][x] = True
    start = graph[y][x]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<n and 0<=ny<n and not visited[ny][nx]:
                current = graph[ny][nx]

                if not blind:
                    if current == start:
                        visited[ny][nx] = True
                        q.append((nx,ny))

                else:
                    if start in ('R', 'G'):
                        if current in ('R', 'G'):
                            visited[ny][nx] = True
                            q.append((nx,ny))
                    else:
                        if current == 'B':
                            visited[ny][nx] = True
                            q.append((nx,ny))

visited1 = [[False]*n for _ in range(n)]
normal = 0
for y in range(n):
    for x in range(n):
        if not visited1[y][x]:
            bfs(x,y,visited1,blind=False)
            normal +=1

visited2 = [[False]*n for _ in range(n)]
blind = 0
for y in range(n):
    for x in range(n):
        if not visited2[y][x]:
            bfs(x,y,visited2,blind=True)
            blind+=1

print(normal, blind)