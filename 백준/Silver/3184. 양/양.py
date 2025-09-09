import sys
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

r,c = map(int, input().split())
graph = []
visited = [[False]*c for _ in range(r)]
for _ in range(r):
    graph.append(list(sys.stdin.readline().strip()))

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[y][x] = True

    sheep = 0
    wolf = 0

    if graph[y][x] == 'o':
        sheep += 1
    if graph[y][x] == 'v':
        wolf += 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<= nx < c and 0<= ny < r and not visited[ny][nx] and graph[ny][nx] != '#':
                visited[ny][nx] = True
                if graph[ny][nx] == 'o':
                    sheep+=1
                elif graph[ny][nx] == 'v':
                    wolf+=1
                q.append((nx,ny))
    return sheep, wolf

total_sheep = 0
total_wolf = 0

for y in range(r):
    for x in range(c):
        if graph[y][x] != '#' and not visited[y][x]:
            s,w = bfs(x,y)
            if s > w:
                total_sheep+=s
            else:
                total_wolf+=w
print(total_sheep, total_wolf)