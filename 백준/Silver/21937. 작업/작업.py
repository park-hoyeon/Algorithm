from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)

visited = [False] * (n+1)

x = int(input())
stack = [x]
visited[x] = True

while stack:
    now = stack.pop()
    for next in graph[now]:
        if not visited[next]:
            visited[next] = True
            stack.append(next)

print(visited.count(True) - 1)