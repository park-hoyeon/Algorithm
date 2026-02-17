n,m = map(int, input().split())

groups = {}
member_group = {}

for _ in range(n):
    team = input().strip()
    member = int(input())
    names = [input().strip() for _ in range(member)]
    names.sort()

    groups[team] = names

    for name in names:
        member_group[name] = team

for _ in range(m):
    q = input().strip()
    type = int(input())

    if type == 0:
        for name in groups[q]:
            print(name)
    else:
        print(member_group[q])