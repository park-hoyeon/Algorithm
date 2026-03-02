import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
answer = 0

for i in range(n):
    answer += abs(data[i] - (i+1))

print(answer)