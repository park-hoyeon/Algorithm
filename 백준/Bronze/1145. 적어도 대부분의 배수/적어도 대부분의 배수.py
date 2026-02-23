import sys
input = sys.stdin.readline

n = list(map(int, input().split()))

num = min(n)
while True:
    count = 0
    for i in n:
        if num % i == 0:
            count += 1

    if count >= 3:
        print(num)
        break
    num += 1