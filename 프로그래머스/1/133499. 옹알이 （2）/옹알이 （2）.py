def solution(babbling):
    answer = 0
    
    word = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        temp = i
        
        if "ayaaya" in temp or "yeye" in temp or "woowoo" in temp or "mama" in temp:
            continue
        
        for j in word:
            temp = temp.replace(j," ")
        
        if temp.strip() == "":
            answer += 1
    
    return answer