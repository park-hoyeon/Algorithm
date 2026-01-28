n,m = map(int, input().split())
nums = list(map(int, input().split()))
answer = [0] * (n+1)
for i in range(n):
    answer[i+1] = answer[i] + nums[i]

for _ in range(m):
    a,b = map(int, input().split())
    print(answer[b] - answer[a-1])