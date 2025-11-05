n = int(input())
num_list = [i for i in range(1,n+1)]
visited = [False] * n
answer = []

def dfs():
    if len(answer) == n:
        print(*answer)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(num_list[i])
            dfs()
            answer.pop()
            visited[i] = False
dfs()