n,m = map(int, input().split())

store = []

def dfs(depth):
    if depth == m:
        print(*store)
        return

    for i in range(1, n+1):
        store.append(i)
        dfs(depth+1)
        store.pop()

dfs(0)
