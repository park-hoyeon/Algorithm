n = int(input())
data = []
for _ in range(n):
    x,y = list(map(int, input().split()))
    data.append((x,y))

data.sort()

start, end = data[0]
answer = 0

for x,y in data[1:]:
    if x <= end:
        end = max(end,y)
    else:
        answer += end - start
        start, end = x,y

answer += end - start
print(answer)