n = int(input())
score = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    max_v = score[i]
    min_v = score[i]

    for j in range(i,n):
        max_v = max(max_v, score[j])
        min_v = min(min_v, score[j])

        if i == 0:
            prev = 0
        else:
            prev = dp[i-1]

        dp[j] = max(dp[j], prev + (max_v - min_v))

print(dp[n-1])