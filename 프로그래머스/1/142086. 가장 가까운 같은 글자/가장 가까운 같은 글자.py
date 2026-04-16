def solution(s):
    answer = []
    
    for i in range(len(s)):
        found = False
        
        for j in range(i-1,-1,-1):
            if s[i] == s[j]:
                answer.append(i-j)
                found = True
                break
                
        if not found:
            answer.append(-1)
        
    return answer