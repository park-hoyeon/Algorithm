n = int(input())

answer = []
for _ in range(n):
    answer.append(input().strip())

for i in range(1,len(answer[0])+1):
    data = set()

    for num in answer:
        data.add(num[-i:])

    if len(data) == n:
        print(i)
        break