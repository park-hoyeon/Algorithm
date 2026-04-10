import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

def dfs(x,y,rain):
    if x < 0 or x>= n or y < 0 or y >= n:
        return False
    
    if visited[x][y]:
        return False
    
    if graph[x][y] <= rain:
        return False

    visited[x][y] = True

    dfs(x-1,y,rain)
    dfs(x+1,y,rain)
    dfs(x,y-1,rain)
    dfs(x,y+1,rain)
    return True

max_h = 0
for x in range(n):
    for y in range(n):
        if graph[x][y] > max_h:
            max_h = graph[x][y]

answer = 0
for rain in range(max_h+1):
    visited = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if dfs(i,j,rain):
                count += 1
    answer = max(answer,count)
print(answer)