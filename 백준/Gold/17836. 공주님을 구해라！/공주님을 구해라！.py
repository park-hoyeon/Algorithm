from collections import deque
import sys
input = sys.stdin.readline

n,m,t = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
q.append((0,0,0))
visited[0][0] = True
answer = int(1e9)

while q:
    x,y,time = q.popleft()
    if time > t:
        continue

    if x == n-1 and y == m-1:
        answer = min(answer, time)

    if graph[x][y] == 2:
        dist = (n-1-x) + (m-1-y)
        answer = min(answer, time+dist)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = True
                q.append((nx,ny,time+1))
if answer <= t:
    print(answer)
else:
    print("Fail")