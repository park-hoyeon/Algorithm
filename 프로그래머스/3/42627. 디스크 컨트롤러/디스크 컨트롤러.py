import heapq

def solution(jobs):
    jobs.sort()
    n = len(jobs)
    
    time = 0
    finish = 0 
    total = 0
    idx = 0
    heap = []
    
    while finish < n:
        while idx < n and jobs[idx][0] <= time:
            req,dur = jobs[idx]
            heapq.heappush(heap, (dur,req))
            idx += 1
        
        if heap:
            dur, req = heapq.heappop(heap)
            time += dur
            total += (time - req)
            finish += 1
        
        else:
            time = jobs[idx][0]
    
    return total // n
    
    
        
        