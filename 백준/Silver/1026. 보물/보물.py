N = int(input())
num1 = list(map(int,input().split()))
num2 = list(map(int, input().split()))

num1.sort()
num2.sort()
num2.reverse()
answer = []

for i in range(N):
    answer.append(num1[i]*num2[i])

print(sum(answer))