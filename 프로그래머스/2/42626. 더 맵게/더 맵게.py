import heapq

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
        
    count = 0
    while len(heap) > 1 and heap[0] < K:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        new = first + (second*2)
        heapq.heappush(heap,new)
        count += 1
        
    if heap[0] >= K:
        return count
    else:
        return -1
            
                        