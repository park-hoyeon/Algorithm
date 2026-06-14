def solution(order):
    
    stack1 = []
    stack2 = []
    n = len(order)
    count = 0
    
    for i in range(n,0,-1):
        stack1.append(i)
    
    for target in order:
        
        if stack2 and stack2[-1] == target:
            stack2.pop()
            count += 1
        
        else:
            while stack1 and stack1[-1] != target:
                stack2.append(stack1.pop())

            if stack1 and stack1[-1] == target:
                stack1.pop()
                count += 1

            else:
                break
        
    return count
            