def solution(left, right):
    answer = 0
    
    for num in range(left,right+1):
        is_answer = False
        i = 1
        
        while i*i <= num:
            if i*i == num:
                is_answer = True
                break
            i += 1
        
        if is_answer == True:
            answer -= num
        else:
            answer += num
    return answer
            