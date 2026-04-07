from collections import deque

n,k = map(int, input().split())
MAX = 100001
dist = [-1] * MAX
count = [0] * MAX

q = deque()
q.append(n)
dist[n] = 0
count[n] = 1

while q:
    x = q.popleft()

    for nx in (x-1,x+1,x*2):
        if 0<=nx<MAX:
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                count[nx] = count[x]
                q.append(nx)

            elif dist[nx] == dist[x] + 1:
                count[nx] += count[x]
print(dist[k])
print(count[k])