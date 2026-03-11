l = int(input())
s = list(map(int, input().split()))
n = int(input())
s.sort()

if n in s:
    print(0)
else:
    left = 0
    right = 0
    
    for i in s:
        if i < n:
            left = i
        elif i>n:
            right = i
            break
    
    print((n-left) * (right-n) -1)