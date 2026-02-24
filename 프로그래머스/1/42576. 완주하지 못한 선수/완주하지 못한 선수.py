def solution(participant, completion):
    
    answer = {}
    
    for person in participant:
        if person in answer:
            answer[person] += 1
        else:
            answer[person] = 1
    
    for i in completion:
        answer[i] -= 1
    
    for name in answer:
        if answer[name] > 0:
            return name
            