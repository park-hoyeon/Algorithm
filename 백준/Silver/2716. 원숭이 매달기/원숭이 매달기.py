n = int(input())
for _ in range(n):
    data = input().strip()

    depth = 0
    max_depth = 0

    for i in data:
        if i == '[':
            depth += 1
            if depth > max_depth:
                max_depth = depth
        else:
            depth -= 1

    print(2**max_depth)