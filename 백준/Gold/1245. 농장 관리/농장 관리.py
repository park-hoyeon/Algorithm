import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, -1, -1,  0, 0, 1, 1, 1]
dy = [-1,  0,  1, -1, 1,-1, 0, 1]

count = 0

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        if graph[i][j] == 0:
            continue

        height = graph[i][j]

        q = deque()
        q.append((i,j))
        visited[i][j] = 1

        is_peak = True

        while q:
            x,y = q.popleft()
            for d in range(8):
                nx = dx[d] + x
                ny = dy[d] + y
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] > height:
                        is_peak = False

                    if not visited[nx][ny] and graph[nx][ny] == height:
                        visited[nx][ny] = 1
                        q.append((nx,ny))

        if is_peak:
            count += 1

print(count)