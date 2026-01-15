import sys
input = sys.stdin.readline

INF = int(1e9)

v,e = map(int, input().split())
dist = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c

for k in range(1,v+1):
    dist_k = dist[k]

    for i in range(1,v+1):
        dist_i = dist[i]
        dist_i_k = dist_i[k]
        if dist_i_k == INF:
            continue

        for j in range(1,v+1):
            dist_k_j = dist_k[j]
            if dist_k_j == INF:
                continue

            new_dist = dist_i_k + dist_k_j
            if new_dist < dist_i[j]:
                dist_i[j] = new_dist

answer = min(dist[i][i] for i in range(1,v+1))
print(-1 if answer == INF else answer)