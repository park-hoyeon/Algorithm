def solution(k, tangerine):
    data = {}
    for i in tangerine:
        if i not in data:
            data[i] = 1
        else:
            data[i] += 1
    
    counts = sorted(data.values(), reverse = True)
    
    total = 0
    answer = 0
    
    for i in counts:
        total += i
        answer += 1
        if total >= k:
            break
    return answer