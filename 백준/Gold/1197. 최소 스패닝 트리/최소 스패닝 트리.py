import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v,e = map(int, input().split())
parent = [0] * (v+1)

def find_parent(parent,x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent,a,b):
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1,v+1):
    parent[i] = i

data = []
for _ in range(e):
    a,b,cost = map(int, input().split())
    data.append((cost,a,b))
data.sort()

answer = 0
for cost,a,b in data:

    ra = find_parent(parent,a)
    rb = find_parent(parent,b)

    if ra != rb:
        union(parent,ra,rb)
        answer += cost

print(answer)   