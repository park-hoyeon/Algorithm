def solution(topping):
    answer = 0
    
    left = {}
    right = {}
    
    for i in topping:
        if i in right:
            right[i] += 1
        else:
            right[i] = 1
    
    for i in topping:
        if i in left:
            left[i] += 1
        else:
            left[i] = 1
        
        right[i] -= 1
        if right[i] == 0:
            del right[i]
    
        if len(left) == len(right):
            answer += 1
    return answer
    
    