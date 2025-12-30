t = int(input())
words_list = []

for i in range(t):
    words_list.append(input())

    freq = {}

    for j in words_list[i]:
        if j == ' ': continue

        if j in freq:
            freq[j] += 1
        else:
            freq[j] = 1

    max_count = max(freq.values())

    candidates = []
    for i,j in freq.items():
        if j == max_count:
            candidates.append(i)

    if len(candidates) > 1: print('?')
    else: print(candidates[0])


