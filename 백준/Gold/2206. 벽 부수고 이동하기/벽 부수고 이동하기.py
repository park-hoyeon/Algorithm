from collections import deque
#시작하는 칸과 끝나는 칸 포함해서 count하기
#벽 한 개까지 부수기 가능
n,m = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
visited1 = [[0]*m for _ in range(n)]    #벽 안 부숨
visited2 = [[0]*m for _ in range(n)]    #벽 부숨

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():

    q = deque()
    q.append((0,0,0))
    visited1[0][0] = 1

    while q:
        x,y,broken = q.popleft()

        if x == n-1 and y == m-1:
            if broken == 0:
                return visited1[x][y]
            else:
                return visited2[x][y]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m:
                if broken == 0:
                    if visited1[nx][ny] == 0 and graph[nx][ny] == 0:
                        visited1[nx][ny] = visited1[x][y] + 1
                        q.append((nx,ny,0))
                    elif graph[nx][ny] == 1 and visited2[nx][ny] == 0:
                        visited2[nx][ny] = visited1[x][y] + 1
                        q.append((nx,ny,1))
                else:
                    if graph[nx][ny] == 0 and visited2[nx][ny] == 0:
                        visited2[nx][ny] = visited2[x][y] + 1
                        q.append((nx,ny,1))
    return -1

print(bfs())                           