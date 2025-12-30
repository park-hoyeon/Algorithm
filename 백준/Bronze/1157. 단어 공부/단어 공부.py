word = input()
new = word.upper()
freq = {}
for i in new:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

    max_count = max(freq.values())

candidates = []
for i,j in freq.items():
    if j == max_count:
        candidates.append(i)

if len(candidates) > 1:
    print('?')
else: print(candidates[0])