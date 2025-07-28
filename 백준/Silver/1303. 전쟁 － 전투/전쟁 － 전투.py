from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

w,h = map(int, input().split())
graph = [list(map(str,input().strip())) for _ in range(h)]
visited = [[False]*w for _ in range(h)]
ours = []
yours = []

def bfs1(x,y):
    q = deque()
    q.append((x,y))
    visited[y][x] = True
    our = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<w and 0<=ny<h and not visited[ny][nx] and graph[ny][nx] == 'W':
                our+=1
                visited[ny][nx] = True
                q.append((nx,ny))

    return our

def bfs2(x,y):
    q = deque()
    q.append((x,y))
    visited[y][x] = True
    you = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<w and 0<=ny<h and not visited[ny][nx] and graph[ny][nx] == 'B':
                you+=1
                visited[ny][nx] = True
                q.append((nx,ny))

    return you


for y in range(h):
    for x in range(w):
        if graph[y][x] == 'W' and not visited[y][x]:
            ours.append(bfs1(x,y))
        if graph[y][x] == 'B' and not visited[y][x]:
            yours.append(bfs2(x,y))

print(sum(i*i for i in ours), sum(i*i for i in yours))