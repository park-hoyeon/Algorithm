data = list(map(int,input().split()))
answer = []
for i in data:
    answer.append(i**2)

result = sum(answer)%10
print(result)