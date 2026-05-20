def solution(files):
    answer = []
    
    for i in files:
        head = ""
        number = ""
        tail = ""
        
        idx = 0
        
        while idx < len(i) and not i[idx].isdigit():
            head += i[idx]
            idx += 1
        
        while idx < len(i) and i[idx].isdigit():
            number += i[idx]
            idx += 1
        tail = i[idx:]
        
        answer.append([head,number,tail])
    
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
        
    result = []
    for h,n,t in answer:
        result.append(h+n+t)
    return result 
    

