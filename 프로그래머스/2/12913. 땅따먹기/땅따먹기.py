def solution(land):
    answer = 0
    n = 0
    
    for i in land:
        n += 1
    
    dp = [[0]*4 for _ in range(n)]
    
    for a in range(4):
        dp[0][a] = land[0][a]
        
    for row in range(1,n):
        for col in range(4):
            max_num = 0
            
            for prev in range(4):
                if prev != col:
                    max_num = max(max_num, dp[row-1][prev])
        
            dp[row][col] = land[row][col] + max_num
            
    return max(dp[n-1])