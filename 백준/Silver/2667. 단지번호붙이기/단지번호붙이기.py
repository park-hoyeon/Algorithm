from collections import deque

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

answer = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            q = deque()
            q.append((i,j))
            visited[i][j] = 1
            count = 1

            while q:
                x,y = q.popleft()
                
                for a in range(4):
                    nx = dx[a] + x
                    ny = dy[a] + y
                    if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                        visited[nx][ny] = 1
                        q.append((nx,ny))
                        count += 1
            answer.append(count)
answer.sort()
print(len(answer))

for i in answer:
    print(i)