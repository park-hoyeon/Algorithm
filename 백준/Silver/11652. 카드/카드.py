n = int(input())
freq = {}
nums = []
for i in range(n):
    nums.append(int(input()))

for i in nums:
    if i in freq: freq[i]+=1
    else: freq[i] = 1
max_count = max(freq.values())

candidates = []
for i,j in freq.items():
    if j == max_count:
        candidates.append(i)
if len(candidates)>1:
    print(min(candidates))
else: print(candidates[0])