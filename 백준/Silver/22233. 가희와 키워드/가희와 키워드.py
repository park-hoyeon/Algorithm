import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dic = set()
word = []
write = []
for _ in range(n):
    word.append(input().strip())
for _ in range(m):
    write.append(list(input().strip().split(',')))

for i in word:
    dic.add(i)

for j in write:
    for k in j:
        dic.discard(k)
    print(len(dic))