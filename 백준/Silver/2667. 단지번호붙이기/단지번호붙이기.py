from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[y][x] = True
    global house
    house = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y


            if 0<= nx < n and 0<=ny<n and not visited[ny][nx] and graph[ny][nx] == 1:
                house+=1
                visited[ny][nx] = True
                q.append((nx, ny))
    return house


n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
count = 0
house_list=[]

for y in range(n):
    for x in range(n):
        if graph[y][x] == 1 and not visited[y][x]:
            count+=1
            house_list.append(bfs(x,y))

print(count)
for i in sorted(house_list):
    print(i)