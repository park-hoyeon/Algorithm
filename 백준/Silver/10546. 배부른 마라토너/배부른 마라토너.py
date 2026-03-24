from itertools import count

n = int(input())

success = {}
for _ in range(n):
    name = input()

    if name in success:
        success[name] += 1
    else:
        success[name] = 1

for _ in range(n-1):
    name2 = input()
    if name2 in success:
        success[name2] -= 1

for i in success:
    if success[i] != 0:
        print(i)