import sys
sys.setrecursionlimit(10000) 

graph = [list(map(str, input().split())) for _ in range(5)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
result = []


def dfs(x,y,n):
    n += graph[y][x]

    if len(n) == 6:
        if n not in result:
            result.append(n)
        return

    for i in range(4):
        nx = dx[i]+ x
        ny = dy[i] + y

        if 0<= nx < 5 and 0<= ny < 5:
            dfs(nx,ny,n)

for i in range(5):
    for j in range(5):
        dfs(i,j,"")

print(len(result))