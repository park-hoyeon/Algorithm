from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

x,y,size = 0,0,2

# 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j

def bfs(x,y,size):
    # 이동한 위치가 graph 안에 있는지 확인하고 해당 좌표가 방문했는지 확인하기
    # 해당 좌표에 있는 물고기 size가 상어 크기보다 작거나 같다면 queue에 좌표 추가
    # 만약 그 좌표가 0이 아니고 상어보다 작다면 먹을 수 있는 list에 추가
    # 먹을 수 있는 list를 정렬시킨 후 반환하기 = (거리,y,x) 좌표순으로 내림차순 하고 pop

    distance = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    tmp = []

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            # 이동 가능한지 확인
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                # 지나갈 수 있는 칸인가
                if graph[nx][ny] <= size:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cur_x][cur_y] + 1

                    # 먹을 수 있는 물고기인가?
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        tmp.append((nx, ny, distance[nx][ny]))

    return sorted(tmp, key=lambda x: (-x[2], -x[0], -x[1]))

count = 0
answer = 0

while True:
    shark = bfs(x,y,size)
    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()

    # 이동한 거리만큼 시간 더하기
    answer += dist

    # 이전 위치 비우기(상어가 떠났으니까 빈 칸), 상어 위치 이동(물고기 먹었으니까 빈 칸)
    graph[x][y], graph[nx][ny] = 0,0

    # 상어 좌표를 먹은 물고기 좌표로 옮기기
    x,y = nx, ny
    count+=1
    if count == size:
        size+=1
        count = 0
print(answer)