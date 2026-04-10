from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())    # 편의점 개수
    places = [] #좌표
    for _ in range(n+2):
        x,y = map(int, input().split())
        places.append((x,y))

    visited = [False] * (n+2)   #장소 방문 여부

    def bfs():
        q =deque()
        q.append(0) #집의 인덱스
        visited[0] = True

        while q:
            now = q.popleft()
            x,y = places[now]

            if abs(x-places[n+1][0]) + abs(y-places[n+1][1]) <= 1000:
                return "happy"
            
            for i in range(n+2):
                if not visited[i]:
                    nx,ny = places[i]

                    if abs(x-nx) + abs(y-ny) <= 1000:
                        visited[i] = True
                        q.append(i)
        return "sad"
    print(bfs())