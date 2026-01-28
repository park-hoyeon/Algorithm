word = input().strip()
find = input()
stack = []
length = len(find)

for i in word:
    stack.append(i)
    if len(stack) >= length and ''.join(stack[-length:]) == find:
        for _ in range(length):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")