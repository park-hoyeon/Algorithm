n,m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

check = min(n,m)
answer = 0

for i in range(n):
    for j in range(m):
        for k in range(check):
            if ((i+k)<n) and (j+k) < m and (graph[i][j] == graph[i][j+k] == graph[i+k][j] ==  graph[i+k][j+k]):
                answer = max(answer, (k+1)**2)
print(answer)