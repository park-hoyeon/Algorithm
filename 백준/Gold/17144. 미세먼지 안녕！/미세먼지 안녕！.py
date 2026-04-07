from collections import deque

n,m,t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 공기청정기 위치
robot = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == -1:
            robot.append((i,j))

top = robot[0][0]
bottom = robot[1][0]

#미세먼지 확산
def spread():
    temp = [[0]*m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if graph[x][y] > 0:
                dust = graph[x][y] // 5
                count = 0

                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if 0<=nx<n and 0<=ny<m and graph[nx][ny] != -1:
                        temp[nx][ny] += dust
                        count += 1
                
                temp[x][y] += graph[x][y] - dust * count
    
    temp[top][0] = -1
    temp[bottom][0] = -1

    return temp

#공기청정기 작동
def air():
    for i in range(top-1,0,-1):
        graph[i][0] = graph[i-1][0]
    
    for i in range(m-1):
        graph[0][i] = graph[0][i+1]
    
    for i in range(top):
        graph[i][m-1] = graph[i+1][m-1]
    
    for i in range(m-1,1,-1):
        graph[top][i] = graph[top][i-1]

    graph[top][1] = 0

    for i in range(bottom+1,n-1):
        graph[i][0] = graph[i+1][0]
    
    for i in range(m-1):
        graph[n-1][i] = graph[n-1][i+1]
    
    for i in range(n-1, bottom, -1):
        graph[i][m-1] = graph[i-1][m-1]
    
    for i in range(m-1,1,-1):
        graph[bottom][i] = graph[bottom][i-1]
    
    graph[bottom][1] = 0

    graph[top][0] = -1
    graph[bottom][0] = -1

for _ in range(t):
    graph = spread()
    air()

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] > 0:
            answer += graph[i][j]

print(answer)