import heapq

def solution(n, works):
    answer = 0
    count = 0
    
    works = [-x for x in works]
    heapq.heapify(works)
    
    while count < n:
        last = -(heapq.heappop(works))
        
        if last == 0:
            break
            
        last -= 1
        heapq.heappush(works,-last)
        count += 1
        
    for data in works:
        answer += (data**2)
    
    return answer
