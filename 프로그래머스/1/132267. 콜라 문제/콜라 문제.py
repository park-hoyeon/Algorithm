def solution(a, b, n):
    answer = 0
    
    while (n >= a):
        remain = n%a
        new = (n//a) * b
        
        answer += new
        n = new + remain
        
    return answer