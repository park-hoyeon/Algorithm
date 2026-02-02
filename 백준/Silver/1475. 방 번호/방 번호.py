n = input().strip()

num_list = [0] * 10

for i in n:
    digit = int(i)
    if digit == 6 or digit == 9:
        num_list[6] += 1
    else:
        num_list[digit] += 1

num_list[6] = (num_list[6] + 1) // 2

print(max(num_list))