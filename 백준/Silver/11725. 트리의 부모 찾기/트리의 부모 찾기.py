import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
board = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b, = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

visited = [0] * (n+1)

def bfs(start):
    q = deque([start])
    visited[start] = -1

    while q:
        node = q.popleft()
        for i in board[node]:
            if visited[i] == 0:
                visited[i] = node
                q.append(i)
bfs(1)
answer = visited[2:]
for d in answer:
    print(d)