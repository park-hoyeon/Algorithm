from collections import deque

n = int(input())
m = int(input())

data = [[] for _ in range(n+1)]
for _ in range(1, m+1):
    a,b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

dist = [-1] * (n+1)
dist[1] = 0

q = deque([1])

while q:
    current = q.popleft()
    if dist[current] == 2:
        continue

    for next in data[current]:
        if dist[next] == -1:
            dist[next] = dist[current] + 1
            q.append(next)

answer = sum(1 for i in range(1,n+1) if dist[i] in (1,2))
print(answer)
