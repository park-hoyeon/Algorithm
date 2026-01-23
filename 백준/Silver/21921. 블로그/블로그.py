import sys
input = sys.stdin.readline

n,x = map(int, input().split())
people = list(map(int, input().split()))

current = sum(people[:x])
max_sum = current
count = 1

for i in range(x,n):
    current = current - people[i-x] + people[i]

    if current > max_sum:
        max_sum = current
        count = 1
    elif current == max_sum:
        count+=1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)