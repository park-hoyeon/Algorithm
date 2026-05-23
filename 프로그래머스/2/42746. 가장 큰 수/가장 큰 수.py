def solution(numbers):
    
    sorted_list = list(map(str, numbers))
    
    sorted_list.sort(key = lambda x: x * 3, reverse = True)
    
    answer = ''.join(sorted_list)
    return str(int(answer))