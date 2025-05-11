S = list(input())
count_0 = 0
count_1 = 0

if S[0] == '0': count_0 += 1
else: count_1 += 1

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        if S[i+1] == "0":
            count_0 += 1
        else:
            count_1 += 1

print(min(count_0, count_1))