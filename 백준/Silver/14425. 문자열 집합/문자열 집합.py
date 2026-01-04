n, m = map(int, input().split())
words = []
check = []
for _ in range(n):
    words.append(input())
for _ in range(m):
    check.append(input())

count = 0
for i in check:
    if i in words:
        count += 1
print(count)