def solution(k, dungeons):
    
    visited = [False] * len(dungeons)
    
    def dfs(k):
        max_count = 0
        
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                count = 1 + dfs(k-dungeons[i][1])
                visited[i] = False
                
                max_count = max(max_count, count)
        return max_count
    
    return dfs(k)
        