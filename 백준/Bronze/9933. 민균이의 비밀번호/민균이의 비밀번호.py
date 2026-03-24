n = int(input())
words = set()

for _ in range(n):
    word = input()
    words.add(word)
    reverse = word[::-1]

    if reverse in words:
        print(len(word), word[len(word)//2])
        break