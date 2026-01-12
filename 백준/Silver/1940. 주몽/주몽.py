import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
num = list(map(int, input().split()))
num.sort()

answer = 0
left, right = 0, n-1

while left < right:
    sum = num[left] + num[right]
    if sum == m:
        answer+=1
        left+=1
        right-=1
    elif sum < m:
        left+=1
    else:
        right-=1
print(answer)