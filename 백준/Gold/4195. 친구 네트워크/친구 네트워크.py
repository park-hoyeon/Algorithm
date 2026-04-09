t = int(input())
for _ in range(t):
    f = int(input())

    parent = {}
    size = {}

    def find_parent(parent,x):
        if parent[x] != x:
            parent[x] = find_parent(parent,parent[x])
        return parent[x]

    def union(parent,a,b):
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a != b:
            if a < b:
                parent[b] = a
                size[a] += size[b]
                return size[a]
            else:
                parent[a] = b
                size[b] += size[a]
                return size[b]
        return size[a]
        
    for _ in range(f):
        a,b = input().split()
        
        if a not in parent:
            parent[a] = a
            size[a] = 1

        if b not in parent:
            parent[b] = b
            size[b] = 1

        print(union(parent,a,b))