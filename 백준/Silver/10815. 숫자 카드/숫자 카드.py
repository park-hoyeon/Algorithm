n = int(input())
has = list(map(int, input().split()))
m = int(input())
has_or_not = list(map(int, input().split()))

count = {}

for i in has:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1

answer = []
for j in has_or_not:
    answer.append(str(count.get(j,0)))
    
print(" ".join(answer))