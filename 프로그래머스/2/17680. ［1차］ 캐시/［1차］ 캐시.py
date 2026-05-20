def solution(cacheSize, cities):
    answer = []
    time = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for i in cities:
        i = i.lower()
        
        if i not in answer:
            time += 5
            
            if len(answer) == cacheSize:
                answer.pop(0)
            answer.append(i)
            
        else:
            time += 1
            answer.remove(i)
            answer.append(i)
    
    return time                    