from collections import Counter

n = int(input())
size = list(map(int, input().split()))
count = Counter(size)

print(max(count.values()))