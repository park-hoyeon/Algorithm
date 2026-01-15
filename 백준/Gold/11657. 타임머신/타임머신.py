import sys
input = sys.stdin.readline

INF = int(1e9)

n,m = map(int, input().split())
data = []
for _ in range(m):
    a,b,c = map(int, input().split())
    data.append((a,b,c))

dist = [INF] * (n+1)
dist[1] = 0

for _ in range(n-1):
    updated = False
    for a,b,c in data:
        if dist[a] != INF and dist[b] > dist[a] + c:
            dist[b] = dist[a] + c
            updated = True
    if not updated:
        break

has_neg_cycle = False
for a,b,c in data:
    if dist[a] != INF and dist[b] > dist[a] + c:
        has_neg_cycle = True
        break

if has_neg_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])