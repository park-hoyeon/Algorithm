from collections import deque

def solution(x, y, n):
    
    q = deque()
    start = x
    q.append((start,0))
    
    visited = set()
    visited.add(start)
        
    while q:
        num, count = q.popleft()
        
        if num == y:
            return count
        
        next_nums = [num + n, num * 2, num * 3]
        
        for next in next_nums:
            if next <= y and next not in visited:
                visited.add(next)
                q.append((next,count+1))
    
    return -1