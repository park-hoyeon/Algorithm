import sys
input = sys.stdin.readline

num = 1
while True:
    line = input()
    if line == "":
        break

    data = line.strip()

    if '-' in data:
        break

    stack = []
    count = 0

    for i in data:
        if i == '{':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                count += 1
                stack.append('{')

    count += len(stack) // 2

    print(str(num) + ". " + str(count))
    num += 1