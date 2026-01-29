n = int(input())
graph = [list(input().strip()) for _ in range(n)]

def check():
    best = 1

    for i in range(n):
        count = 1
        for j in range(1,n):
            if graph[i][j] == graph[i][j-1]:
                count += 1
                best = max(best, count)
            else:
                count = 1

    for b in range(n):
        count_ = 1
        for a in range(1,n):
            if graph[a][b] == graph[a-1][b]:
                count_ += 1
                best = max(best, count_)
            else:
                count_ = 1

    return best

answer = check()

for i in range(n):
    for j in range(n):
        if j+1 < n and graph[i][j] != graph[i][j+1]:
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            answer = max(answer, check())
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]

        if i+1<n and graph[i][j] != graph[i+1][j]:
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
            answer = max(answer, check())
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
print(answer)