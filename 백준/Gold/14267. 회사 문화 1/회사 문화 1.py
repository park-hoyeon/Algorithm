import sys
input = sys.stdin.readline

n,m = map(int, input().split())
up = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for i in range(2,n+1):
    parent = up[i-1]
    graph[parent].append(i)

score = [0] * (n+1)

for _ in range(m):
    i,w = map(int, input().split())
    score[i] += w

stack = [1]

while stack:
    x = stack.pop()
    for nx in graph[x]:
        score[nx] += score[x]
        stack.append(nx)

print(*score[1:])