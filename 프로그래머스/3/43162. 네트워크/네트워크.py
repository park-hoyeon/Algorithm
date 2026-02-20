def solution(n, computers):
    visited = [False] * n
    
    def dfs(start):
        visited[start] = True
        
        for i in range(n):
            if computers[start][i] == 1 and not visited[i]:
                dfs(i)
    
    count = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    
    return count