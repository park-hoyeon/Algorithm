n = int(input())
minus = [0] + list(map(int, input().split()))
plus = [0] + list(map(int, input().split()))

dp = [ [-1]*101 for _ in range (n+1)]
dp[0][100] = 0

for i in range(1, n+1):
    for j in range(100, -1, -1):
        if dp[i - 1][j] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
        if j+minus[i] <= 100 and dp[i-1][j+minus[i]] != -1: #남은 체력 있어야 함.
            dp[i][j] = max(dp[i][j], dp[i-1][j+ minus[i]]+plus[i] )
joy = max(dp[n][1:101])
print(joy)