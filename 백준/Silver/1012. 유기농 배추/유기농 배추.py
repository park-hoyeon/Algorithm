import sys
sys.setrecursionlimit(10000)

def find(x,y):
    visited[y][x] = True    #현재 위치 방문처리함

    #이동 방향: 상하좌우
    dx = [0,0,-1,+1]
    dy = [-1,+1,0,0]

    # 방향 탐색
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<M and 0<=ny<N and graph[ny][nx] == 1 and not visited[ny][nx]:
            find(nx,ny)

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    # 배추밭과 방문한 배열 초기화
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        X,Y = map(int,input().split())
        graph[Y][X] = 1

    # 배추 구역 카운트 개수
    worm = 0

    # 배추밭 탐색하기
    for j in range(N):
        for i in range(M):
            #배추가 있는데 아직 방문 X
            if graph[j][i] == 1 and not visited[j][i]:
                find(i,j)
                worm += 1
    print(worm)




