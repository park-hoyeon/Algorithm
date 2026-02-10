def solution(n):
    arr = []
    for i in str(n):
        arr.append(i)
        
    arr.sort(reverse=True)        
    return int(''.join(arr))