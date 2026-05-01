import heapq

def solution(n, road, k):
    INF = int(1e9)
    
    distance = [INF] * (n+1)
    
    graph = [[] for _ in range(n+1)]
    for i in range(len(road)):
        a = road[i][0]
        b = road[i][1]
        c = road[i][2]
        
        graph[a].append((b,c))
        graph[b].append((a, c))
    
    def dijkstra(start):
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
    dijkstra(1)
    
    answer = 0
    for i in distance:
        if i <= k:
            answer += 1
    return answer