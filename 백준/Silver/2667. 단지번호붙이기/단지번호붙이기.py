from collections import deque

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    total = 1
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx,ny))
                total += 1
    return total

answer = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            answer.append(bfs(i,j))
answer.sort()
print(len(answer))
for x in answer:
    print(x)