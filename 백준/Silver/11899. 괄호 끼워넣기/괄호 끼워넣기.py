from collections import deque
import sys
input = sys.stdin.readline

s = input().strip()
q = deque(s)
store = []
less = 0

while q:
    a = q.popleft()
    if a == '(':
        store.append(a)
    else:
        if store:
            store.pop()
        else:
            less += 1

print(len(store) + less)