n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = graph[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j==0:
            continue

        up = 0
        left = 0
        diag = 0

        if i > 0:
            up = dp[i-1][j]
        if j > 0:
            left = dp[i][j-1]
        if i>0 and j>0:
            diag = dp[i-1][j-1]

        dp[i][j] = max(up,left,diag) + graph[i][j]

print(dp[n-1][m-1])
        