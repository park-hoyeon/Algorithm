def solution(numbers):
    data = 0
    for i in range(10):
        if i not in numbers:
            data += i
            
    return data