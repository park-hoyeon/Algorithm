import sys
input = sys.stdin.readline

n = int(input())
names = []
result = []

for _ in range(n):
    name = input()
    names.append(name[0])
first_names = set(names)

for i in first_names:
    if names.count(i) >= 5:
        result.append(i)

result.sort()
if result:
    print("".join(result))
else:
    print("PREDAJA")