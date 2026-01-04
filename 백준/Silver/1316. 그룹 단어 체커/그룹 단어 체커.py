n = int(input())
words = []
answer = 0
for i in range(n):
    words.append(input())

    used = []
    prev = ''
    for j in words[i]:
        if j != prev:
            if j in used:
                break
            used.append(j)
        prev = j
    else:
        answer+=1
print(answer)