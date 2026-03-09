n = int(input())

pos = []
neg = []
one = 0
zero = 0

for _ in range(n):
    data = int(input())

    if data > 1:
        pos.append(data)
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        neg.append(data)

pos.sort(reverse=True)
neg.sort()

answer = 0

for i in range(0,len(pos),2):
    if i+1 < len(pos):
        answer += pos[i] * pos[i+1]
    else:
        answer += pos[i]

for j in range(0,len(neg),2):
    if j+1 < len(neg):
        answer += neg[j] * neg[j+1]
    else:
        if zero == 0:
            answer += neg[j]

answer += one

print(answer)
