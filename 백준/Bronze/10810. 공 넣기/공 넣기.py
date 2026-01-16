import sys
input = sys.stdin.readline

n,m = map(int, input().split())
bag = [0]*(n+1)

for _ in range(m):
    i,j,k = map(int, input().split())
    for d in range(i,j+1):
        bag[d] = k

for i in range(1,n+1):
    print(bag[i], end=" ")