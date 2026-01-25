import sys
input = sys.stdin.readline

graph = []
for _ in range(8):
    graph.append(list(input().strip()))

count = 0
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            if graph[i][j] == 'F':
                count+=1
print(count)