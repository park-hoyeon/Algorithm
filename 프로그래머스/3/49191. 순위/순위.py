def solution(n, results):
    
    INF = int(1e9)
    
    graph = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        graph[i][i] = 0
        
    for win,lose in results:
        graph[win-1][lose-1] = 1
    
    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                
    answer = 0
    
    for i in range(n):
        count = 0
        for j in range(n):
            if graph[i][j] != INF or graph[j][i] != INF:
                count += 1
        
        if count == n:
            answer += 1
    
    return answer
                
    