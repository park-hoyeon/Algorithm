import heapq

def solution(n, s, a, b, fares):
    INF = int(1e9)
    
    graph = [[] for _ in range(n+1)]
    
    for x, y, cost in fares:
            graph[x].append((y,cost))
            graph[y].append((x,cost))
    
    def dijkstra(start):
        dist = [INF] * (n+1)
        
        q = []
        heapq.heappush(q,(0,start))
        dist[start] = 0
        
        while q:
            d,now = heapq.heappop(q)
            
            if dist[now] < d:
                continue
            
            for next_node, fare in graph[now]:
                cost = d + fare
                if cost < dist[next_node]:
                    dist[next_node] = cost
                    heapq.heappush(q,(cost,next_node))
        
        return dist

    dist_s = dijkstra(s)
    dist_a = dijkstra(a)
    dist_b = dijkstra(b)
    
    answer = INF
    
    for i in range(1,n+1):
        answer = min(answer, dist_s[i] + dist_a[i] + dist_b[i])
    
    return answer