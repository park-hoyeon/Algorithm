n = int(input())
pair = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(pair):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def dfs(x):
    global count
    if not visited[x]:
        visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            count += 1
            dfs(i)

    return count

print(dfs(1))      