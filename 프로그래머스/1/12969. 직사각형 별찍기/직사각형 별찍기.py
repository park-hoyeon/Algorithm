a, b = map(int, input().strip().split(' '))

graph = ['*'*a for _ in range(b)]

print('\n'.join(graph))