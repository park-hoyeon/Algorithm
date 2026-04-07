t = int(input())
for _ in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(graph[0][0], graph[1][0]))
        continue

    graph[0][1] += graph[1][0]
    graph[1][1] += graph[0][0]

    for i in range(2,n):
        graph[0][i] += max(graph[1][i-1], graph[1][i-2])
        graph[1][i] += max(graph[0][i-1], graph[0][i-2])

    print(max(graph[0][n-1], graph[1][n-1]))