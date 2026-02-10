from collections import deque

n = int(input())
r1,c1,r2,c2 = map(int, input().split())

dist = [[-1]*n for _ in range(n)]
dist[r1][c1] = 0

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

q = deque()
q.append((r1,c1))

while q:
    r,c = q.popleft()

    if r == r2 and c == c2:
        break

    for i in range(6):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0<= nr < n and 0<=nc<n and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr,nc))

print(dist[r2][c2])