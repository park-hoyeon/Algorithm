from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

while True:
    a,b = map(int, input().split())
    if a == -1 and b == -1:
        break

    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

score = [0] * (n+1)

for i in range(1,n+1):
    score[i] = max(graph[i][1:n+1])

min_score = min(score[1:])

answer = []
for i in range(1,n+1):
    if score[i] == min_score:
        answer.append(i)
print(min_score, len(answer))
print(*answer)