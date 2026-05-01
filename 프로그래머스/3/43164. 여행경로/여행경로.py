def solution(tickets):
    answer = []
    
    visited = [False] * len(tickets)
    tickets.sort()
    
    def dfs(current,path):
        
        if len(path) == len(tickets) + 1:
            return path
    
        for i in range(len(tickets)):
            start,end = tickets[i]

            if not visited[i] and start == current:
                visited[i] = True
            
                result = dfs(end, path+[end])
                if result:
                    return result
            
                visited[i] = False
                
    return dfs("ICN", ["ICN"])