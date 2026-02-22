from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque()

for _ in range(n):
    data = list(map(int, input().split()))

    if data[0] == 1:
        dq.appendleft(data[1])
    elif data[0] == 2:
        dq.append(data[1])
    elif data[0] == 3:
        print(dq.popleft() if dq else -1)
    elif data[0] == 4:
        print(dq.pop() if dq else -1)
    elif data[0] == 5:
        print(len(dq))
    elif data[0] == 6:
        print(0 if dq else 1)
    elif data[0] == 7:
        print(dq[0] if dq else -1)

    elif data[0] == 8:
        print(dq[-1] if dq else -1)