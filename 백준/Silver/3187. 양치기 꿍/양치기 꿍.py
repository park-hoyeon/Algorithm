from collections import deque
import sys
input = sys.stdin.readline

r,c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]

dn = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(n,y):
    q = deque()
    q.append((n,y))
    visited[n][y] = True

    sheep = 0
    wolf = 0

    if graph[n][y] == 'k':
        sheep += 1
    elif graph[n][y] == 'v':
        wolf += 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dn[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] != '#':
                visited[nx][ny] = True
                if graph[nx][ny] == 'k':
                    sheep += 1
                elif graph[nx][ny] == 'v':
                    wolf += 1
                q.append((nx,ny))

    if sheep > wolf:
        return sheep,0
    else:
        return 0,wolf

total_s = 0
total_w = 0

for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j] != '#':
            s,w = bfs(i,j)
            total_s += s
            total_w += w

print(total_s, total_w)

