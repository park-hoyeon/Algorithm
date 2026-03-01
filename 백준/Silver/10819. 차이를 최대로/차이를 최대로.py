n = int(input())
num = list(map(int, input().split()))

used = [False] * n
store = []
best = 0

def dfs(depth):
    global best

    if depth == n:
        current_score = 0
        for i in range(n-1):
            current_score += abs(store[i] - store[i+1])
        best = max(best, current_score)

    for i in range(n):
        if not used[i]:
            used[i] = True
            store.append(num[i])

            dfs(depth+1)

            store.pop()
            used[i] = False
            
dfs(0)
print(best)