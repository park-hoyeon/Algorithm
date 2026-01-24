import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()
for _ in range(n):
    data = input().split()
    if data[0] == 'push_back':
        q.append(data[1])
    elif data[0] == 'push_front':
        q.appendleft(data[1])
    elif data[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif data[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(q))
    elif data[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif data[0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
