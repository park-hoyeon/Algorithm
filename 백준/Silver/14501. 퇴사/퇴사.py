n = int(input())
dp = [0 for i in range(n+1)]
day = []
money = []
max_value = 0

for _ in range(n):
    t,p = map(int, input().split())
    day.append(t)
    money.append(p)

for i in range(n):
    dp[i+1] = max(dp[i+1], dp[i])

    end = i + day[i]
    if end <= n:
        dp[end] = max(dp[end], dp[i]+money[i])
print(dp[n])