n,l = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort()

count = 0
start = 0

for i in pos:
    if start < i:
        count += 1
        start = i - 0.5 + l

print(count)