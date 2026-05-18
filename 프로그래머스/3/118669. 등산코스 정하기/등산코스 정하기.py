import heapq

def solution(n, paths, gates, summits):
    answer = []
    
    INF = int(1e9)
    
    graph = [[] for i in range(n+1)]
    for i in paths:
        a = i[0]
        b = i[1]
        c = i[2]
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    gate_set = set(gates)
    summit_set = set(summits)
    
    def dijkstra(start):
        distance = [INF] * (n+1)
        q = []
        
        for gate in gates:
            distance[gate] = 0
            heapq.heappush(q,(0,gate))
        
        while q:
            dist, now = heapq.heappop(q)
            
            if distance[now] < dist:
                continue
                
            if now in summit_set:
                continue
            
            for i in graph[now]:
                next_node = i[0]
                weight = i[1]
                
                if next_node in gate_set:
                    continue
                
                cost = max(dist, weight)
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q,(cost,next_node))
        
        for summit in summit_set:
            answer.append((summit,distance[summit]))
        
    dijkstra(gates[0])
        
    answer.sort(key=lambda x: (x[1],x[0]))
        
    return answer[0]
    