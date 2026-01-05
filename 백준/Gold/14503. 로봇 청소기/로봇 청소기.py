import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

n,m = map(int, input().split())
r,c,d = map(int, input().split())
area = []
for _ in range(n):
    area.append(list(map(int, input().split())))

def dfs(x,y,d):
    global count

    if area[x][y] == 0:
        area[x][y] = 2
        count += 1

    for _ in range(4):
        d = (d-1) % 4
        nx = dx[d] + x
        ny = dy[d] + y

        if area[nx][ny] == 0:
            dfs(nx, ny, d)
            return

    back_dir = (d+2)%4
    bx = dx[back_dir] + x
    by = dy[back_dir] + y

    if area[bx][by] == 1:
        return

    dfs(bx,by,d)

dfs(r,c,d)
print(count)