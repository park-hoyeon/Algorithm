s = input()
n = len(s)

a_count = s.count('a')

if a_count == 0 or a_count == n:
    print(0)
else:
    answer = 1000

    for start in range(n):
        b_count = 0

        for i in range(start, start + a_count):
            if s[i%n] == 'b':
                b_count += 1

        answer = min(answer, b_count)
    print(answer)