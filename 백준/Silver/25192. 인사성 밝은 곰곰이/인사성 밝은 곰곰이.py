import sys
input = sys.stdin.readline

n = int(input().strip())
data = set()
count = 0

for _ in range(n):
    person = input().strip()
    if person == 'ENTER':
        data.clear()
    else:
        if person not in data:
            data.add(person)
            count+=1
print(count)