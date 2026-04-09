n = int(input())
pair = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(pair):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited[start] = True

    for next in graph[start]:
        if not visited[next]:
            dfs(next)
dfs(1)
print(visited.count(True) - 1)