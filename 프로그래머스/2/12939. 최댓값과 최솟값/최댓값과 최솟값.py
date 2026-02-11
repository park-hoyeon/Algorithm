def solution(s):
    answer = []
    for i in s.split():
        answer.append(int(i))
    min_num = min(answer)
    max_num = max(answer)
    
    return str(min_num) + " " + str(max_num)