def solution(intStrs, k, s, l):
    answer = []
    
    for i in intStrs:
        save = i[s:s+l]

        if int(save) > k:
            answer.append(int(save))
    return answer