n = int(input())
dp = [0 for i in range(n+1)]
day = []
money = []
max_value = 0

for _ in range(n):
    t,p = map(int, input().split())
    day.append(t)
    money.append(p)

for i in range(n-1,-1, -1):
    if i + day[i] <= n:
        dp[i] = max(money[i]+dp[i+day[i]], max_value)
    else:
        dp[i] = max_value
    max_value = dp[i]
print(max_value)