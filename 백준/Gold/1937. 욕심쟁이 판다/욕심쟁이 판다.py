import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] > graph[x][y]:
            dp[x][y] = max(dp[x][y], 1+dfs(nx,ny))
    return dp[x][y]

answer = 0

for i in range(n):
    for j in range(n):
        answer = max(answer,dfs(i,j))

print(answer)