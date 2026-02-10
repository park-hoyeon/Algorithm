import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    applicants = []

    for _ in range(n):
        a,b = map(int, input().split())
        applicants.append((a,b))
    applicants.sort()

    count = 1
    best = applicants[0][1]

    for i in range(1,n):
        if applicants[i][1] < best:
             count += 1
             best = applicants[i][1]
    print(count)