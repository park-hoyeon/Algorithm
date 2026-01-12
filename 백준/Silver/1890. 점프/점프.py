import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            continue
        jump = graph[i][j]
        if jump == 0:
            continue

        ni = i + jump
        nj = j + jump

        if ni < n:
            dp[ni][j] +=dp[i][j]
        if nj < n:
            dp[i][nj] += dp[i][j]
print(dp[n-1][n-1])