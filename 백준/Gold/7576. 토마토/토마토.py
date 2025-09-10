from collections import deque
import sys

dx = [0,0,-1,1]
dy = [-1,1,0,0]

m,n = map(int,input().split())
graph = []
visited = [[False]*m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

q = deque()
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            q.append((x,y))
            visited[y][x] = True

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=ny<n and 0<=nx<m and graph[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                graph[ny][nx] = graph[y][x] + 1
                q.append((nx,ny))
bfs()

answer = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            print(-1)
            sys.exit(0)
        answer = max(answer, graph[y][x])
print(answer-1)