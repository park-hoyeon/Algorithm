from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<w and 0<= ny < h:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = graph[y][x]+1
                    q.append((nx, ny))

h,w = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(h)]

bfs(0,0)
print(graph[h-1][w-1])
