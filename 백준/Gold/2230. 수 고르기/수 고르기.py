import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

i,j = 0,0
answer = float('inf')

while i<n and j<n:
    diff = arr[j] - arr[i]

    if diff < m:
        j+=1
    else:
        answer = min(answer, diff)
        i += 1
print(answer)
