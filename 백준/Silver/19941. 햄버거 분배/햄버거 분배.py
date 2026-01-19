import sys

input = sys.stdin.readline

n,k = map(int, input().split())
data = list(input())
count = 0

for i in range(n):
    if data[i] == "P":
        for j in range(i-k,i+k+1):
            if 0<=j<n and data[j] == "H":
                count+=1
                data[j] = "0"
                break

print(count)