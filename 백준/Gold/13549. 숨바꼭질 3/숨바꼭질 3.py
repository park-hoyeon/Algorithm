from collections import deque

n,k = map(int, input().split())
MAX = 1000000

def bfs(n,k):
    dist = [-1] * (MAX+1)
    q = deque()
    q.append(n)
    dist[n] = 0

    while q:
        x = q.popleft()

        if x == k:
            return dist[x]
        
        next2 = x*2
        if 0 <= next2 <= MAX and dist[next2] == -1:
                dist[next2] = dist[x]
                q.append(next2)

        for next in (x-1,x+1):
            if 0 <= next <= MAX and dist[next] == -1:
                dist[next] = dist[x]  + 1
                q.append(next)

    return dist[k]
print(bfs(n,k))