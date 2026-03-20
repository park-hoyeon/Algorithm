from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
w,h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]

dx1 = [-1, 1, 0, 0]
dy1 = [0, 0, -1, 1]

dx2 = [-2, -2, -1, -1, 1, 1, 2, 2]
dy2 = [-1, 1, -2, 2, -2, 2, -1, 1]

q = deque()
q.append((0,0,0))
visited[0][0][0] = 0

while q:
    x,y,used = q.popleft()

    if x == h-1 and y == w-1:
        print(visited[x][y][used])
        break

    for i in range(4):
        nx = x + dx1[i]
        ny = y + dy1[i]

        if 0 <= nx < h and 0 <= ny < w:
            if visited[nx][ny][used] == -1 and graph[nx][ny] == 0:
                visited[nx][ny][used] = visited[x][y][used] + 1
                q.append((nx,ny,used))

    if used < k:
        for i in range(8):
            nx = x + dx2[i]
            ny = y + dy2[i]

            if 0<=nx<h and 0<=ny<w:
                if graph[nx][ny] == 0 and visited[nx][ny][used+1] == -1:
                    visited[nx][ny][used+1] = visited[x][y][used] + 1
                    q.append((nx, ny, used + 1))

else:
    print(-1)