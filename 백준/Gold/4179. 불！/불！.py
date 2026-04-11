from collections import deque

r,c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited1 = [[0]*c for _ in range(r)]
visited2 = [[0]*c for _ in range(r)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def fire():
    q = deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'F':
                q.append((i,j))
                visited1[i][j] = 1
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<r and 0<=ny<c:
                #벽,지훈이 아닌 칸으로 확산
                if graph[nx][ny] == '.' and visited1[nx][ny] == 0:
                    visited1[nx][ny] = visited1[x][y] + 1
                    q.append((nx,ny))

def move():
    q = deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'J':
                q.append((i,j))
                visited2[i][j] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            #탈출
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                return visited2[x][y]

            #불 아닌 칸 + 벽 아닌 칸으로 이동
            if graph[nx][ny] != '#' and visited2[nx][ny] == 0:
                #불 보다 먼저 가야 함.
                if visited1[nx][ny] == 0 or visited2[x][y] + 1 < visited1[nx][ny]:
                    visited2[nx][ny] = visited2[x][y] + 1
                    q.append((nx,ny))
    
    return "IMPOSSIBLE"

fire()
print(move())