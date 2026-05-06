from collections import deque

def solution(q1, q2):
    answer = 0
    
    q1 = deque(q1)
    q2 = deque(q2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    total = sum1 + sum2
    
    if total % 2 == 1:
        return -1
    
    limit = total // 2
    max_count = (len(q1) + len(q2)) * 2
    
    while answer < max_count:
        
        if sum1 == limit:
            return answer
        
        if sum1 > limit:
            start1 = q1.popleft()
            q2.append(start1)
            sum1 -= start1
            sum2 += start1
        
        else:
            start2 = q2.popleft()
            q1.append(start2)
            sum1 += start2
            sum2 -= start2
        
        answer += 1
    
    return -1
    
    