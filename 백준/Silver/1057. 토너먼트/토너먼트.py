import sys
input = sys.stdin.readline

num,ji,han = map(int, input().split())

count = 0
while ji != han:
    ji -= ji//2
    han -= han//2
    count+=1
print(count)