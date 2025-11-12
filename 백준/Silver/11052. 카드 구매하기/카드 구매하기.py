n = int(input())
cards = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
max_value = 0

for i in range(1,n+1):
    best = 0
    for j in range(1,i+1):
        best = max(cards[j-1] + dp[i-j], best)
    dp[i] = best
print(dp[n])