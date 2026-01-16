import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

row = [False] * n
col = [False] * m

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'X':
            row[i] = True
            col[j] = True

row_need = row.count(False)
col_need = col.count(False)

print(max(row_need,col_need))