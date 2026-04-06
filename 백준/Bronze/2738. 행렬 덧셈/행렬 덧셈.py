n,m = map(int, input().split())
graph1 = [list(map(int, input().split())) for _ in range(n)]
graph2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(graph1[i][j] + graph2[i][j], end=" ")
    print()
