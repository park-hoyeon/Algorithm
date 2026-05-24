def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x: x[1])
    
    target = -1
    
    for i in targets:
        if target < i[0]:
            target = i[1] - 0.1
            answer += 1
            
    return answer