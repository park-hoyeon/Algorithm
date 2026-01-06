import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            house.append((x, y))
        elif graph[x][y] == 2:
            chicken.append((x,y))

answer = float('inf')
dist = [[0]*len(chicken) for _ in range(len(house))]
for i, (hx,hy) in enumerate(house):
    for j, (cx,cy) in enumerate(chicken):
        dist[i][j] = abs(hx-cx) + abs(hy-cy)
for comb in combinations(range(len(chicken)), m):
    city = 0
    for i in range(len(house)):
        city += min(dist[i][j] for j in comb)
    answer = min(answer,city)
print(answer)