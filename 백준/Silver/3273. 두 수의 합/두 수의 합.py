import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
x = int(input())
data.sort()

left = 0
right = n-1
count = 0

while left < right:
    s = data[left] + data[right]

    if s == x:
        count+=1
        left+=1
        right-=1
    elif s<x:
        left+=1
    else:
        right-=1
print(count)
