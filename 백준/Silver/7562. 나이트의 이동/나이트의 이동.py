from collections import deque

t = int(input())
for _ in range(t):
    l = int(input())
    now_x,now_y = map(int, input().split())
    goal_x,goal_y = map(int,input().split())

    visited = [[-1]*l for _ in range(l)]

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    def bfs():
        q = deque()
        q.append((now_x,now_y))
        visited[now_x][now_y] = 0

        while q:
            x,y = q.popleft()

            if x == goal_x and y == goal_y:
                return visited[x][y]
            
            for i in range(8):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0<=nx<l and 0<=ny<l:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx,ny))
    
    print(bfs())