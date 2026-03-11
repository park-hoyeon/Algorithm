n,c = map(int, input().split())
nums = list(map(int, input().split()))
dic = {}
for i in nums:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

answer = []
for j in dic:
    answer.append((j,dic[j]))

answer.sort(key=lambda x: -x[1])

for num, cnt in answer:
    for _ in range(cnt):
        print(num, end=' ')