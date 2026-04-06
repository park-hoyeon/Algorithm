n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
store = [[0]*m for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

answer = 0

empty = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i,j))

def virus(x,y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<n and 0<=ny<m and store[nx][ny] == 0:
            store[nx][ny] = 2
            virus(nx,ny)

def get_scale():
    scale = 0
    for i in range(n):
        for j in range(m):
            if store[i][j] == 0:
                scale += 1
    return scale

def dfs(start,count):
    global answer
    if count == 3:
        for i in range(n):
            for j in range(m):
                store[i][j] = graph[i][j]
        
        for i in range(n):
            for j in range(m):
                if store[i][j] == 2:
                    virus(i,j)
        
        answer = max(answer, get_scale())
        return 

    for i in range(start,len(empty)):
        x,y = empty[i]
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(i+1, count+1)
            graph[x][y] = 0
        
dfs(0,0)
print(answer)