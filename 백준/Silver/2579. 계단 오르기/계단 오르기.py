# 계단오르기
n = int(input())
array=[]
for _ in range(n):
    array.append(int(input()))
if n == 0: print(0)
else:
    dp = [0] * n
    if n == 1:
        print(array[0])
    elif n == 2:
        print(array[0]+array[1])
    else:
        dp[0] = array[0]
        dp[1] = array[0]+array[1]
        dp[2] = max(array[0]+array[2], array[1]+array[2])
        for i in range(3, n):
            dp[i] = max(dp[i-3] + array[i-1] + array[i], dp[i-2]+array[i])
        print(dp[n-1])