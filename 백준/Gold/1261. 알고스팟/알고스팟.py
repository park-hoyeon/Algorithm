from collections import deque

m,n = map(int, input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append((0,0))
    visited[0][0] = 0

    while q:
        x,y = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y]
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                #벽 없는 경로는 그냥 가기
                if graph[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] 
                    q.appendleft((nx,ny))
    
                #벽이 있으면 벽 부수기 -> broken 카운트하기
                elif graph[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    return 0
print(bfs(0,0))