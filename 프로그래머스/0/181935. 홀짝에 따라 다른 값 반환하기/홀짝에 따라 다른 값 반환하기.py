def solution(n):
    answer = []
    answer2 = []
    
    if n%2 == 1:
        for i in range(1,n+1):
            if i%2 == 1:
                answer.append(i)
        return (sum(answer))
    else:
        for j in range(1,n+1):
            if j % 2 == 0:
                answer2.append(j**2)
        return (sum(answer2))