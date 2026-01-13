import sys
input = sys.stdin.readline

n = int(input())
times = []

for _ in range(n):
    start, end = map(int, input().split())
    times.append((start, end))
times.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in times:
    if start >= end_time:
        count+=1
        end_time = end

print(count)