n = int(input())
cards = list(map(int, input().split()))
dp = cards

for i in range(n):
    for j in range(1,i+1):
        dp[i] = min(dp[i], dp[i-j]+cards[j-1])
print(dp[n-1])