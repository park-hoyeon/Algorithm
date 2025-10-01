import sys
input = sys.stdin.readline
n, m = map(int, input().split())
words = {}

for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        words[word] = words.get(word, 0) + 1

print(*sorted(words, key=lambda x:[-words[x], -len(x), x]), sep='\n')