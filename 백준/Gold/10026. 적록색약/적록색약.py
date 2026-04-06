from collections import deque

n = int(input())
graph1 = [list(input().strip()) for _ in range(n)]
graph2 = [row[:] for row in graph1]


dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(x,y,graph):
    q = deque()
    q.append((x,y))
    color = graph[x][y]
    graph[x][y] = 'V'

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == color:
                graph[nx][ny] = 'V'
                q.append((nx,ny))

count1 = 0
for i in range(n):
    for j in range(n):
        if graph1[i][j] != 'V':
            bfs(i,j,graph1)
            count1 += 1

for i in range(n):
    for j in range(n):
        if graph2[i][j] == 'G':
            graph2[i][j] = 'R'

count2 = 0
for i in range(n):
    for j in range(n):
        if graph2[i][j] != 'V':
            bfs(i,j,graph2)
            count2 += 1
print(count1, count2)