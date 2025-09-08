from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

n,m,k = map(int, input().split())
visited = [[False]*m for _ in range(n)]
graph = [[0]*m for _ in range(n)]
for _ in range(k):
    r,c = map(int, input().split())
    graph[r-1][c-1] = 1

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[y][x] = True
    count = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y

            if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and graph[ny][nx] == 1:
                count +=1
                visited[ny][nx] = True
                q.append((nx,ny))
    return count

answer = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1 and not visited[y][x]:
            answer = max(answer, bfs(x,y))
print(answer)

