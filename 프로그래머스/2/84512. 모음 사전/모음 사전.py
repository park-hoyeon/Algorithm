def solution(word):
    global answer
    answer = 0
    
    words = ["A", "E", "I", "O", "U"]
    
    def dfs(now):
        global answer
        
        if now == word:
            return True
        
        if len(now) == 5:
            return False
        
        for i in words:
            answer += 1
            
            if dfs(now+i):
                return True
        
        return False
    
    dfs("")
    return answer