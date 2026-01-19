import sys
input = sys.stdin.readline

n = int(input())
students = []
for _ in range(n):
    students.append(int(input()))
dp = [1]*n

for i in range(n):
    for j in range(i):
        if students[i] > students[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))