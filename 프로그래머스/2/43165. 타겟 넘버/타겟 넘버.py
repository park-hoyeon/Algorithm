def solution(numbers, target):
    answer = 0
    
    def dfs(index,sum_num):
        nonlocal answer
        
        if index == len(numbers):
            if sum_num == target:
                answer += 1
            return
        
        dfs(index+1,sum_num + numbers[index])
        dfs(index+1,sum_num - numbers[index])
        
    dfs(0,0)
    
    return answer