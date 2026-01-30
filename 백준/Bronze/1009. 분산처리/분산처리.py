import sys
input = sys.stdin.readline

n = int(input())
answer = []

for _ in range(n):
    a,b = map(int, input().split())
    result = pow(a, b, 10)
    
    if result == 0:
        print(10)
    else:
        print(result)