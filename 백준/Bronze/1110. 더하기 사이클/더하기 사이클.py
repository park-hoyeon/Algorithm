n = int(input())

original = n
count = 0

while True:
    a = n//10
    b = n%10
    new = b*10 + (a+b)%10
    
    count += 1
    n = new
    
    if n == original:
        break

print(count)