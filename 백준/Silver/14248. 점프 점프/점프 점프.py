from collections import deque

n = int(input())
dist = list(map(int, input().split()))
s = int(input()) - 1

visited = [False] * n

stack = deque()
stack.append(s)
visited[s] = True

while stack:
    x = stack.pop()
    for next in [x+dist[x], x-dist[x]]:
        if 0 <= next < n and not visited[next]:
            visited[next] = True
            stack.append(next)

print(visited.count(True))
