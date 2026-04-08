import sys
input = sys.stdin.readline

n,m = map(int, input().split())

parent = [0] * (n+1)

def find_parent(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
 
def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    sign,a,b = map(int, input().split())
    if sign == 0:
        union(a,b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")