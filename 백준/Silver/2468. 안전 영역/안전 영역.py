from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y,h):
    q =  deque()
    q.append((x,y))
    visited[y][x] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y

            if 0<=nx<n and 0<=ny<n and not visited[ny][nx] and graph[ny][nx] > h:
                visited[ny][nx] = True
                q.append((nx, ny))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_len = max(map(max, graph))
result = 0

for h in range(0,max_len+1):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if graph[y][x] > h and not visited[y][x]:
                bfs(x,y,h)
                count+=1
    result = max(result, count)
print(result)