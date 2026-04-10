from collections import deque

f,s,g,u,d = map(int, input().split())
MAX = 10**6

def bfs(s,g):
    dist = [-1] * (MAX+1)
    q = deque([s])
    dist[s] = 0

    while q:
        x = q.popleft()

        if x == g:
            return dist[x]
    
        for next in (x-d,x+u):
            if 1<=next<=f and dist[next] == -1:
                dist[next] = dist[x] + 1
                q.append(next)
    
    return "use the stairs"

print(bfs(s,g))