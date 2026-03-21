from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

q = deque()
q.append((0,0))
visited[0][0] = True

while q:
    x,y = q.popleft()

    if graph[x][y] == -1:
        print("HaruHaru")
        exit()

    jump = graph[x][y]

    nx = x + jump
    ny = y
    if 0 <= nx < n and not visited[nx][ny]:
        visited[nx][ny] = True
        q.append((nx,ny))

    nx = x
    ny = y + jump
    if 0 <= ny < n and not visited[nx][ny]:
        visited[nx][ny] = True
        q.append((nx, ny))

print("Hing")