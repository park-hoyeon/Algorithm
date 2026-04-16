def solution(name, yearning, photo):
    score = {}
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    
    answer = []
    
    for i in photo:
        total = 0
        for j in i:
            if j in score:
                total += score[j]
        answer.append(total)
    return answer
                            