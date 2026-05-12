def solution(numbers):
    answer = 0
    made = set()
    
    def is_prime(data):
        if data < 2:
            return False
        for i in range(2,int(data**0.5)+1):
            if data % i == 0:
                return False
        return True        
    
    def dfs(now,remain):
        nonlocal answer
        
        if now != "":
            number = int(now)
            
            if number not in made:
                made.add(number)
                
                if is_prime(number):
                    answer += 1
        
        for i in range(len(remain)):
            dfs(now+remain[i], remain[:i] + remain[i+1:])
    
    dfs("", numbers)
    
    return answer