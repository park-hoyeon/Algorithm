import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

n,k = map(int, input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j)) #바이러스 종류, 시간, 위치x, 위치y

data.sort()
q = deque(data)

targetS,targetX,targetY = map(int, input().split())

while q:
    virus,s,x,y = q.popleft()
    if s == targetS:
        break

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus,s+1,nx,ny))

print(graph[targetX-1][targetY-1])