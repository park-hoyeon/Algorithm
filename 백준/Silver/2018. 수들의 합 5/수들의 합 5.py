n = int(input())
start, end, count, sum = 1,1,0,1

while start <= n:
    if sum == n:
        count+=1

    if sum >= n:
        sum -= start
        start+=1
    else:
        end+=1
        sum += end

print(count)