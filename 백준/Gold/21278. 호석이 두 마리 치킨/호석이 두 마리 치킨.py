from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

min_sum = INF
answer_a = 0
answer_b = 0

for i in range(1,n+1):
    for j in range(i+1,n+1):
        total = 0

        for k in range(1,n+1):
            total += min(graph[k][i], graph[k][j])

        total *= 2

        if total < min_sum:
            min_sum = total
            answer_a = i
            answer_b = j

print(answer_a, answer_b, min_sum)