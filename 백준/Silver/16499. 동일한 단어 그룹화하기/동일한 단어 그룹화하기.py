n = int(input())
words = set()

for _ in range(n):
    word = input().rstrip()
    words.add(''.join(sorted(word)))

print(len(words))