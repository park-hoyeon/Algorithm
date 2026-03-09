import sys
input = sys.stdin.readline

n = int(input())
names = input().split()
dic = {}

for name in names:
    dic[name] = 0

for _ in range(n):
    votes = input().split()
    for i in votes:
        dic[i] += 1

answer = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
for name, count in answer:
    print(name, count)