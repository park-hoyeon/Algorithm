case_num = 1

while True:
    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break

    parent = [0] * (n+1)

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

    for i in range(1,n+1):
        parent[i] = i

    for _ in range(m):
        a,b = map(int, input().split())

        ra = find_parent(parent,a)
        rb = find_parent(parent,b)

        if ra == rb:
            parent[ra] = 0
        else:
            if ra == 0 or rb == 0:
                parent[ra] = 0
                parent[rb] = 0
            else:
                union(parent,ra,rb)

    tree = set()

    for i in range(1,n+1):
        root = find_parent(parent,i)
        if root != 0:
            tree.add(root)
    
    tree_count = len(tree)

    if tree_count == 0:
        print(f"Case {case_num}: No trees.")
    elif tree_count == 1:
        print(f"Case {case_num}: There is one tree.")
    else:
        print(f"Case {case_num}: A forest of {tree_count} trees.")
    
    case_num += 1