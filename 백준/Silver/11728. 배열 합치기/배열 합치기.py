a,b = map(int, input().split())
a_content = list(map(int, input().split()))
b_content = list(map(int, input().split()))

a_content.extend(b_content)
a_content.sort()
print(*a_content)