import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
    global count
    stack = [(x,y)]
    visited[x][y] = True

    while stack:
        x,y = stack.pop()
        if graph[x][y] == 'P':
            count += 1

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny] != 'X':
                    visited[nx][ny] = True
                    stack.append((nx,ny))

count = 0

found = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            dfs(i,j)
            found = True
            break
    if found:
        break

if count == 0:
    print('TT')
else:
    print(count)