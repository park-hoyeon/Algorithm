import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
data = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    data[b].append(a)

def bfs(x):
    visited = [False] * (n+1)
    visited[x] = True
    q = deque([x])
    count = 1

    while q:
        now = q.popleft()
        for nx in data[now]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
                count += 1

    return count

answer = []
max_value = 0

for i in range(1,n+1):
    cnt = bfs(i)

    if cnt > max_value:
        max_value = cnt
        answer = [i]
    elif cnt == max_value:
        answer.append(i)

print(*answer)