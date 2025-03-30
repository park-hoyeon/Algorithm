# 포도주 시식
n = int(input())
array=[int(input()) for _ in range(n)]
if n==1:
    print(array[0])
else:
    dp=[0]*(n+1)
    dp[0] = array[0]
    if n > 1:
        dp[1] = array[0] + array[1]
    if n > 2:
        dp[2] = max(dp[1], array[0] + array[2], array[1] + array[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + array[i], dp[i - 3] + array[i - 1] + array[i])
    print(dp[n-1])