n=int(input())
inside = set() #리스트 대신 set을 사용해서 시간 초과 방지
for _ in range(n):
    work = input().split()
    name = work[0]
    condition = work[1]

    if condition == "enter":
        inside.add(name)
    elif condition == "leave":
        inside.discard(name)
inside_list = sorted(inside, reverse=True) #역순으로 반환하기
for person in inside_list:
    print(person)