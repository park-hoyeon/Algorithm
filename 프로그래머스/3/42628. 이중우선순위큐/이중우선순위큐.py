import heapq

def solution(operations):
    answer = []
    
    for i in operations:
        word, num = i.split()
        num = int(num)
        
        if word == 'I':
            heapq.heappush(answer, num)
        elif word == 'D':
            if answer:
                if num < 0:
                    heapq.heappop(answer)
                else:
                    answer = [-int(x) for x in answer]
                    heapq.heapify(answer)
                    heapq.heappop(answer)
                    
                    answer = [-x for x in answer]
                    heapq.heapify(answer)
    
    if len(answer) == 0:
        return (0,0)
    else:
        min_num = min(answer)
        max_num = max(answer)

        return (max_num, min_num)