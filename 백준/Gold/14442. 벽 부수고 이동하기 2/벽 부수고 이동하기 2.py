from collections import deque

n,m,k = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]   

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1

    while q:
        x,y,broken = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][broken]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    q.append((nx,ny,broken))
        
        if broken < k:
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1 and visited[nx][ny][broken+1] == 0:
                        visited[nx][ny][broken+1] = visited[x][y][broken] + 1
                        q.append((nx,ny,broken+1))
    return -1
print(bfs())

