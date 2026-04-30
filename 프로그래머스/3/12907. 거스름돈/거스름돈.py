def solution(n, money):
    answer = 0
    dp = [0]*(n+1) #거스름돈 주는 방법 수 (1,2,3원일 때...)
    dp[0] = 1   # dp[1] = 1, dp[2] = 2, dp[3] = 2, dp[4] = 3, dp[5] = 4
    
    for coin in money:
        for i in range(coin,n+1):
            dp[i] += dp[i-coin]
            dp[i] = dp[i] % 1000000007
            
    return dp[n]
        
    