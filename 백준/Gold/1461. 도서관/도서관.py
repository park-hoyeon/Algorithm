n,m = map(int, input().split())
dis = list(map(int, input().split()))

pos = []
neg = []

for i in dis:
    if i > 0:
        pos.append(i)
    else:
        neg.append(abs(i))

pos.sort(reverse=True)
neg.sort(reverse=True)
answer = 0

for i in range(0,len(pos),m):
    answer += pos[i] * 2
for i in range(0,len(neg),m):
    answer += neg[i] * 2

max_dist = 0
if pos:
    max_dist = max(max_dist, pos[0])
if neg:
    max_dist = max(max_dist, neg[0])

answer -= max_dist
print(answer)