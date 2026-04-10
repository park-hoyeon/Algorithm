from collections import deque

m,n,h = map(int, input().split())
graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

dz = [1,-1,0,0,0,0]
dx = [0,0,-1,1,0,0]
dy = [0,0,0,0,-1,1]

tomato = deque()

for a in range(h):
    for i in range(n):
        for j in range(m):
            if graph[a][i][j] == 1:
                tomato.append((a,i,j))

while tomato:   
    z,x,y = tomato.popleft()

    for i in range(6):
        nx = dx[i] + x
        ny = dy[i] + y
        nz = dz[i] + z

        if 0<=nx<n and 0<=ny<m and 0<=nz<h and graph[nz][nx][ny] == 0:
            graph[nz][nx][ny] = graph[z][x][y] + 1
           
            tomato.append((nz,nx,ny))

answer = 0

for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                print(-1)
                exit()
            answer = max(answer, graph[z][x][y])
print(answer-1)