n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = 1

dx = [0, 1]
dy = [1, 0]

for x in range(n):
    for y in range(n):
        if dp[x][y] == 0:
            continue
        if x == n-1 and y == n-1:
            continue

        jump = graph[x][y]

        for i in range(2):
            nx = x + dx[i]*jump
            ny = y + dy[i]*jump

            if 0 <= nx < n and 0 <= ny < n:
                dp[nx][ny] += dp[x][y]
print(dp[n-1][n-1])