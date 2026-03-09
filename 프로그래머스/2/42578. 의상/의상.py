def solution(clothes):
    
    dic = {}
    for a,b in clothes:
        if b in dic:
            dic[b] += 1
        else:
            dic[b] = 1
        
    answer = 1
    for i in dic.values():
        answer *= (i+1)
    
    return (answer-1)
    