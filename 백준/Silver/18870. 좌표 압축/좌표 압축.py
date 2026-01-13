import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

numset = set(data)
a = list(numset)
a.sort()

numdict = {}
for i in range(len(a)):
    numdict[a[i]] = i
for i in data:
    print(numdict[i], end=" ")

