computer = int(input())
pair = int(input())

graph=[[] for _ in range(computer+1)]
visited = [0]*(computer+1)

for _ in range(pair):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def find(value):
    visited[value] = 1
    for i in graph[value]:
        if visited[i] == 0:
            find(i)
    return
find(1)
print(sum(visited)-1)
