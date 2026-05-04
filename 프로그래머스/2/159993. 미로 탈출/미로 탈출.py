from collections import deque

def solution(maps):
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    n = len(maps)
    m = len(maps[0])
    
    start, lever = (0,0), (0,0)
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i,j)
            if maps[i][j] == 'L':
                lever = (i,j)
    
    def bfs(start, target):
        visited = [[0] * m for _ in range(n)]
        
        q = deque()
        q.append(start)
        
        while q:
            x,y = q.popleft()
            
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 > nx or nx >= n or 0 > ny or ny >= m:
                    continue
            
                if maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    
                    if maps[nx][ny] == target:
                        return visited[nx][ny]
                    
                    q.append((nx,ny))
        return -1
    
    dist1 = bfs(start,'L')
    if dist1 == -1:
        return -1
    
    dist2 = bfs(lever,'E')
    if dist2 == -1:
        return -1
    
    return dist1 + dist2