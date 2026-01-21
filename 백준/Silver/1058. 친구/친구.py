n = int(input())
friends = [list(input()) for _ in range(n)]

graph = [[0]*n for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if friends[a][b] == 'Y' or (friends[a][k] == 'Y' and friends[k][b] == 'Y'):
                graph[a][b] = 1

answer = 0
for i in graph:
    answer = max(answer, sum(i))
print(answer)