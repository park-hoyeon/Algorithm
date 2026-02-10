def solution(a, b):
    arr = []
    if a <= b:
        for i in range(a,b+1):
            arr.append(i)
    elif a>b:
        for i in range(b,a+1):
            arr.append(i)
    
    return sum(arr)