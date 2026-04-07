from collections import deque

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dz = [1,-1,0,0,0,0]
dx = [0,0,-1,1,0,0]
dy = [0,0,0,0,-1,1]

q = deque()

for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                q.append((z,x,y))

while q:
    z,x,y = q.popleft()
    for i in range(6):
        nz = dz[i] + z
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nz<h and 0<=nx<n and 0<=ny<m:
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append((nz,nx,ny))
            
answer = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                print(-1)
                exit()
            answer = max(answer, graph[z][x][y])
print(answer-1)