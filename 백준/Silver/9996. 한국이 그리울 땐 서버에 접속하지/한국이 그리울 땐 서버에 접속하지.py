import sys
input = sys.stdin.readline

n = int(input())
pattern = input().strip()
front, back = pattern.split('*')

for _ in range(n):
    file = input().strip()

    if len(file) < len(front) + len(back):
        print("NE")
        continue

    if file.startswith(front) and file.endswith(back):
        print("DA")
    else:
        print("NE")