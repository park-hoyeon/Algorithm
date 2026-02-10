from collections import deque

def solution(priorities, location):
    
    q = deque(priorities)
    answer = 0
    
    while q:
        num = q.popleft()
        if q and num < max(q):
            q.append(num)
            if location == 0:
                location = len(q) - 1
            else:
                location -= 1
        
        else:
            answer += 1
            if location == 0:
                return answer
            else:
                location -= 1
                
                