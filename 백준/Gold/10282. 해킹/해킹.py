import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

t = int(input())

for _ in range(t):
    n,d,c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(d):
        a,b,s = map(int, input().split())
        graph[b].append((a,s))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if dist > distance[now]:
                continue

            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(c)

    count = 0
    max_time = 0
    
    for i in range(1,n+1):
        if distance[i] != INF:
            count += 1
            max_time = max(max_time, distance[i])
    print(count, max_time)
    
    