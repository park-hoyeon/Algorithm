from collections import deque

n,m = map(int, input().split())
x1,y1,x2,y2 = map(int,input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x1,y1))
    visited[x1][y1] = 0

    while q:
        x,y = q.popleft()

        if x == x2 and y == y2:
            return visited[x][y]
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < n and 0 <= ny < m:
                #친구 없으면 (0이면) 그냥 지나가기
                if graph[nx][ny] == '0' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx,ny))
                
                #친구 있으면(1이면) 부수고 가기
                elif graph[nx][ny] == '1' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                
                #바로 도착지점이면
                elif graph[nx][ny] == '#' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

    return -1

print(bfs(0,0))