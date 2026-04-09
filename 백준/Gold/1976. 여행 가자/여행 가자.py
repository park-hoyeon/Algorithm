n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1,n+1):
    row = list(map(int, input().split()))
    for j in range(1,n+1):
        if row[j-1] == 1:
            union(parent,i,j)

plan = list(map(int, input().split()))

root = find_parent(parent,plan[0])

for city in plan:
    if find_parent(parent,city) != root:
        print("NO")
        exit()

print("YES")