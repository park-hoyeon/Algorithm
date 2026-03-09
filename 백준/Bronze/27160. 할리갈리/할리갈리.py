import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for _ in range(n):
    s,x = input().split()
    x = int(x)

    if s in dic:
        dic[s] += x
    else:
        dic[s] = x

for i in dic:
    if dic[i] == 5:
        print("YES")
        break
else:
    print("NO")