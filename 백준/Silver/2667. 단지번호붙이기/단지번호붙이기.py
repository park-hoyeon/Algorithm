n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    if graph[x][y] == 0:
        return 0
    
    graph[x][y] = 0
    count = 1

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        count += dfs(nx,ny)
    return count

answer = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(dfs(i,j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)