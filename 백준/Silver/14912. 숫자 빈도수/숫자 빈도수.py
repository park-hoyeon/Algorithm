n, d = map(int, input().split())
count = 0
for i in range(1,n+1):
    for j in str(i):
        if j == str(d):
            count+=1
print(count)