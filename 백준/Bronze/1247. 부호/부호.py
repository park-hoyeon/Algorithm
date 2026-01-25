import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    count = 0

    for _ in range(n):
        count += int(input())

    if count > 0:
        print('+')
    elif count < 0:
        print('-')
    else:
        print('0')