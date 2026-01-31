import sys
input = sys.stdin.readline

n,k = map(int, input().split())
kind = list(map(int, input().split()))
answer = []
count = 0

for idx in range(k):
    now = kind[idx]

    if now in answer:
        continue
    elif len(answer) < n:
        answer.append(now)
        continue

    next_use = []
    for pulgged in answer:
        if pulgged in kind[idx+1:]:
            next_use.append(kind[idx+1:].index(pulgged))
        else:
            next_use.append(float('inf'))

    remove_index = next_use.index(max(next_use))

    answer.pop(remove_index)
    answer.append(now)
    count += 1

print(count)