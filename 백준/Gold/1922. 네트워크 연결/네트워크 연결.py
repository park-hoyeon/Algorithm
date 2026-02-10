import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

edge = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edge.append((c,a,b))

edge.sort()

parent = [i for i in range(n+1)]

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

total_cost = 0

for cost,a,b in edge:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        total_cost += cost
        
print(total_cost)