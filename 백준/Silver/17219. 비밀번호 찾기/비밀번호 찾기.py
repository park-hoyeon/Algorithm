n,m = map(int, input().split())
answer = {}
for _ in range(n):
    add, pwd = input().split()
    answer[add] = pwd

for _ in range(m):
    title = input().strip()
    print(answer[title])