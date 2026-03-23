import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [-1] * (n+1)
    visited[start] = 0
    q = deque([start])

    while q:
        now = q.popleft()

        for nx in graph[now]:
            if visited[nx] == -1:
                visited[nx] = visited[now] + 1
                q.append(nx)

    return sum(visited[1:])

answer = 0
min_value = int(1e9)

for i in range(1,n+1):
    result = bfs(i)

    if result < min_value:
        min_value = result
        answer = i

print(answer)