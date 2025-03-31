n = int(input())
dp = [float('inf')] * (n+1)
dp[0]=0
sugar_bags = [3,5]
for sugar_bag in sugar_bags:
    for i in range(sugar_bag, n+1):
        if dp[i-sugar_bag] == float('inf'): continue
        dp[i] = min(dp[i], dp[i-sugar_bag]+1)
answer=dp[n] if dp[n]!=float('inf') else -1
print(answer)