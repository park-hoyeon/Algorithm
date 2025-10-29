n = int(input())
lists = []
for _ in range(n):
    lists.append(input())
lists.sort(key= lambda x: (len(x), sum(int(k) for k in x if k.isdigit()), x))
for answer in lists: print(answer)

