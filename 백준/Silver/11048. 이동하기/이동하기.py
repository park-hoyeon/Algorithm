import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = graph[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        dp[i][j] = max(dp[i-1][j]+graph[i][j], dp[i][j-1]+graph[i][j])
print(dp[n-1][m-1])