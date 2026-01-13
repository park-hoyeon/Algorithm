import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
data.sort()

b = [x[1] for x in data]

dp = [1]*n

for i in range(n):
    for j in range(i):
        if b[j] < b[i]:
            dp[i] = max(dp[i], dp[j]+1)

lis = max(dp)
print(n-lis)