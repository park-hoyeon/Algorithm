def solution(answers):
    answer = []
    
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    count1 = 0
    count2 = 0
    count3 = 0
    
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            count1 += 1
        if answers[i] == two[i % len(two)]:
            count2 += 1
        if answers[i] == three[i % len(three)]:
            count3 += 1
    
    max_count = max(count1, count2, count3)
    
    if count1 == max_count:
        answer.append(1)
    if count2 == max_count:
        answer.append(2)
    if count3 == max_count:
        answer.append(3)
    
    return answer
        
        
    
    result = []
    
    result.append(answer.count(1))
    
    return result