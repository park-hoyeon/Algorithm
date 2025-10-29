t = int(input())

def bin(b, n):
    start = 0
    end = len(b)
    while start < end:
        mid = (start+end) // 2
        if n <= b[mid]:
            end = mid
        else: start = mid+1
    return end

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    count = 0
    for i in range(n):
        if a[i] <= b[0]: continue
        elif a[i] > b[-1]: count+=m
        else: count += bin(b,a[i])
    print(count)
