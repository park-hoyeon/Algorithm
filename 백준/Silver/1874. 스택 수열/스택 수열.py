n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
answer = []
start = 1
flag = True

for i in arr:
    while start <= i:
        stack.append(start)
        start+=1
        answer.append("+")
    if stack and stack[-1] == i:
        stack.pop()
        answer.append("-")
    else:
        flag = False
        break

if flag:
    for i in answer:
        print(i)
else: print("NO")


# 4 3 6 8 7 5 2 1