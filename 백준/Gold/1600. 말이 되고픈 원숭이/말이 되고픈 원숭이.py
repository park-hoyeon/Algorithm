from collections import deque

k = int(input())    #움직이는 횟수
w,h = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(h)]
visited = [[[-1]*(k+1) for _ in range(w)] for _ in range(h)]    

hx = [-1,-2,-2,-1,1,2,2,1]
hy = [-2,-1,1,2,2,1,-1,-2]

mx = [0,0,-1,1]
my = [-1,1,0,0]

def bfs():
    q = deque()
    q.append((0,0,0))   #x,y,move
    visited[0][0][0] = 0

    while q:
        x,y,move = q.popleft()

        if x == h - 1 and y == w - 1:
            return visited[x][y][move]
        
        #원숭이 이동
        for i in range(4):
            nx = mx[i] + x
            ny = my[i] + y
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 0 and visited[nx][ny][move] == -1:
                    visited[nx][ny][move] = visited[x][y][move] + 1
                    q.append((nx,ny,move))
        
        #말 이동
        if move < k:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]

                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] == 0 and visited[nx][ny][move+1] == -1:
                        visited[nx][ny][move+1] = visited[x][y][move] + 1
                        q.append((nx,ny,move+1))

    return -1
    
print(bfs())