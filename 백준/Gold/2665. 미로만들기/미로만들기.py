from collections import deque

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 0

    while q:
        x,y = q.popleft()
    
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<n and 0<=ny<n:

                #흰 방이면 그냥 지나가기
                if graph[nx][ny] == 1: 
                    if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y]:
                        visited[nx][ny] = visited[x][y]
                        q.appendleft((nx,ny))
                #검은 방이면 비용+1
                else:
                    if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + 1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx,ny))

    return visited[n-1][n-1]

print(bfs())
