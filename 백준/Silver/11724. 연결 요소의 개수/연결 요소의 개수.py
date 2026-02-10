import sys
input = sys.stdin.readline

n,m = map(int, input().split())

answer = [[]for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    u,v = map(int, input().split())
    answer[u].append(v)
    answer[v].append(u)

def dfs(x):
    visited[x] = True
    for nx in answer[x]:
        if not visited[nx]:
            dfs(nx)

count = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count+=1

print(count)