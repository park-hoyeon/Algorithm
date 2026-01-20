import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())

board = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a,b = map(int, input().split())
    board[a][b] = 1

l = int(input())
turns = {}
for _ in range(l):
    x,c = input().split()
    turns[int(x)] = c

dx = [0,1,0,-1]
dy = [1,0,-1,0]

snake = deque([(1,1)])
board[1][1] = 2

time = 0
dir = 0 #처음엔 오른쪽
x,y = 1,1

while True:
    time+=1
    nx = dx[dir] + x
    ny = dy[dir] + y

    if not (1<=nx<=n and 1<=ny<=n):
        break
    if board[nx][ny] == 2:
        break
    if board[nx][ny] == 1:
        board[nx][ny] = 2
        snake.append((nx,ny))
    else:
        board[nx][ny] = 2
        snake.append((nx,ny))
        tx,ty = snake.popleft()
        board[tx][ty] = 0

    x,y = nx,ny

    if time in turns:
        if turns[time] == 'L':
            dir = (dir + 3)%4
        else:
            dir = (dir + 1)%4
print(time)