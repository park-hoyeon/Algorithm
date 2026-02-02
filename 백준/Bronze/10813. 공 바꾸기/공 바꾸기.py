n,m = map(int, input().split())

graph = []
for i in range(n+1):
    graph.append(i)

for _ in range(m):
    i,j = map(int, input().split())
    graph[i],graph[j] = graph[j], graph[i]

print(*graph[1:])