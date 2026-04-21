def solution(s):
    answer = 0
    
    i = 0
    
    while i < len(s):
        start = s[i]
        same = 0
        diff = 0
        
        while i < len(s):
            if start == s[i]:
                same += 1
            else:
                diff += 1
            i += 1
        
            if same == diff:
                break

        answer += 1
        
    return answer