from collections import deque

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

def dfs(x):
    visited_dfs[x] = True
    print(x, end=" ")

    for next in graph[x]:
        if not visited_dfs[next]:
            dfs(next)

def bfs(start):
    q = deque()
    q.append(start)
    visited_bfs[start ] = True

    while q:
        x = q.popleft()
        print(x, end=" ")
        
        for next in graph[x]:
            if not visited_bfs[next]:
                visited_bfs[next] = True
                q.append(next)

dfs(v)
print()
bfs(v)