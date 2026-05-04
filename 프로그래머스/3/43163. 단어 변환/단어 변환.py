from collections import deque

def solution(begin, target, words):
    
    q = deque()
    q.append((begin,0))
    visited = []
    visited.append(begin)
    
    while q:
        word, count = q.popleft()
        
        if word == target:
            return count
        
        for next in words:
            if next not in visited: 
                
                diff = 0
        
                for i in range(len(begin)):
                    if word[i] != next[i]:
                        diff += 1
                
                if diff == 1:
                    visited.append(next)
                    q.append((next,count+1))
    
    return 0
    