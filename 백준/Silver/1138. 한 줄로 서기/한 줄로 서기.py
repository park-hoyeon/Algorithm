n = int(input())
data = list(map(int, input().split()))

answer = [0] * n

for i in range(n):
    count = data[i]
    for j in range(n):
        if answer[j] == 0 and count > 0:
            count -= 1
        elif answer[j] == 0 and count == 0:
            answer[j] = i+1
            break

print(*answer)