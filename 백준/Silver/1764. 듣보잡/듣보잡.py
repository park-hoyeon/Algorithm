n,m = map(int, input().split())

heard = set()
for _ in range(n):
    heard.add(input().strip())

both = []
for _ in range(m):
    name = input().strip()
    if name in heard:
        both.append(name)

both.sort()
print(len(both))
print("\n".join(both))