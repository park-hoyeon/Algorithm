while True:
    m,n = map(int, input().split())
    if m == 0 and n == 0:
        break

    parent = [0] * (m+1)

    def find_parent(parent,x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union(parent,a,b):
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    for i in range(m):
        parent[i] = i

    data = []
    total = 0

    for _ in range(n):
        x,y,dist = map(int, input().split())
        data.append((dist,x,y))
        total += dist

    data.sort()
    answer = 0

    for cost,x,y in data:
        if find_parent(parent,x) != find_parent(parent,y):
            union(parent,x,y)
            answer += cost

    print(total - answer)