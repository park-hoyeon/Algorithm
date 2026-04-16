def solution(s):
    same = []
    
    for i in s:
        if same and same[-1] == i:
            same.pop()
        else:
            same.append(i)
    
    if len(same) == 0:
        return 1
    else:
        return 0