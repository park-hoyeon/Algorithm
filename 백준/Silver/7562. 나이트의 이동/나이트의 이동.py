from collections import deque

t = int(input())
for _ in range(t):
    l = int(input())
    now_x, now_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())

    dist = [[-1] * l for _ in range(l)]

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    q = deque()
    q.append((now_x, now_y))
    dist[now_x][now_y] = 0

    while q:
        x,y = q.popleft()
        if x == goal_x and y == goal_y:
            print(dist[x][y])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))
