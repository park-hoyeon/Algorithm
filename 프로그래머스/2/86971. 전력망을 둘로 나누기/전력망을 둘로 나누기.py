def solution(n, wires):
    answer = n
    
    graph = [[] for _ in range(n+1)]
    
    for i in wires:
        a = i[0]
        b = i[1]
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(x,visited):
        visited[x] = True
        count = 1
        for i in graph[x]:
            if not visited[i]:
                count += dfs(i,visited)
        return count
    
    for a,b in wires:
        visited = [False] * (n+1)
        visited[b] = True
        
        group1_count = dfs(a,visited)
        group2_count = n - group1_count
        
        diff = abs(group1_count - group2_count)
        answer =  min(answer, diff)
        
    return answer