from collections import deque

n,m = map(int, input().split())
num = list(map(int, input().split()))

q = deque(range(1,n+1))
count = 0

for i in num:
    idx = q.index(i)

    if idx <= len(q) // 2:
        q.rotate(-idx)
        count += idx
    else:
        q.rotate(len(q) - idx)
        count += len(q) - idx

    q.popleft()
print(count)