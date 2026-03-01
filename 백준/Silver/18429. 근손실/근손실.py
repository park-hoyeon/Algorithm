n,k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

used = [False] * n

def dfs(power, depth):
    if power < 500:
        return 0

    if depth == n:
        return 1

    total = 0
    for i in range(n):
        if not used[i]:
            used[i] = True
            total += dfs(power + data[i] - k, depth + 1)
            used[i] = False
    return total

print(dfs(500,0))