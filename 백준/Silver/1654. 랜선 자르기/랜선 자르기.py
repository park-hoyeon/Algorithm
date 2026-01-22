import sys
input = sys.stdin.readline

k,n = map(int, input().split())
data = list(int(input()) for _ in range(k))

start = 1
end = max(data)
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in data:
        count += i // mid

    if count >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)