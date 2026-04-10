n = int(input())
a,b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(x,depth):
    visited[x] = True

    if x == b:
        return depth

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            answer = dfs(i,depth+1)
            if answer != -1:
                return answer
    return -1

print(dfs(a,0))      

