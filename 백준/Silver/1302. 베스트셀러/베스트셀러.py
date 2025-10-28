n = int(input())
books = {}
for _ in range(n):
    title = input()
    if title in books: books[title] += 1
    else: books[title] = 1
max_count = max(books.values())

best_seller = []
for title, cnt in books.items():
    if cnt == max_count:
        best_seller.append(title)
best_seller.sort()
print(best_seller[0])