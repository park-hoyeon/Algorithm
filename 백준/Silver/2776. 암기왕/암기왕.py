import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):

    count = []

    n = int(input())
    note1 = set(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    for i in note2:
        if i in note1:
            count.append(1)
        else:
            count.append(0)

    for k in count:
        print(k)

