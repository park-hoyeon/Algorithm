import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
start = x

for _ in range(m):
    a,b,t = map(int, input().split())
    graph[a].append((b,t))
    reverse_graph[b].append((a,t))

def dijkstra(start,graph):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

go = dijkstra(start,graph)
back = dijkstra(start,reverse_graph)

max_time = 0
for i in range(1,n+1):
    max_time = max(max_time, go[i] + back[i])
print(max_time)