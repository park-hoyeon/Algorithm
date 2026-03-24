import heapq
INF = int(1e9)

n,d = map(int, input().split())
graph = [[] for i in range(d+1)]
distance = [INF] * (d+1)

for i in range(d):
    graph[i].append((i+1,1))

for _ in range(n):
    start, end, l = map(int, input().split())
    if end > d:
        continue
    graph[start].append((end,l))


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

dijkstra(0)
print(distance[d])



