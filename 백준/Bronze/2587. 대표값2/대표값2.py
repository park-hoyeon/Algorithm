import sys
input = sys.stdin.readline

data = []
for _ in range(5):
    data.append(int(input()))
data.sort()
avg = sum(data)/5
mid = data[2]

print(int(avg))
print(mid)
