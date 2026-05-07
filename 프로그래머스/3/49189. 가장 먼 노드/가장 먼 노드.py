from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    distance = [-1] * (n+1)
    
    def bfs(start):
        q = deque()
        q.append(start)
        distance[start] = 0
        
        while q:
            x = q.popleft()
            for next in graph[x]:
                if distance[next] == -1:
                    distance[next] = distance[x] + 1
                    q.append(next)
    
    bfs(1)
                    
    max_distance = max(distance)
    return distance.count(max_distance)