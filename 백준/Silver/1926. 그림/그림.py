from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[y][x] = True
    lens = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<= nx < w and 0<= ny < h:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx, ny))
                    lens += 1
    return lens

h, w = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[False] * w for _ in range(h)]

count = 0
max_lens = 0

for y in range(h):
    for x in range(w):
        if graph[y][x] == 1 and not visited[y][x]:
            lens = bfs(x,y)
            count += 1
            max_lens = max(max_lens, lens)

print(count)
print(max_lens)