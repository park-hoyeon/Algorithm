s = input()
words = []
temp = ""
tag = False

for i in s:
    if i == '<':
        if temp:
            words.append(temp[::-1])
            temp = ""
        tag = True
        temp += i
    elif i == '>':
        temp += i
        words.append(temp)
        temp = ""
        tag = False
    elif tag:
        temp+=i

    else:
        if i == ' ':
            words.append(temp[::-1])
            words.append(' ')
            temp = ""
        else:
            temp+=i
if temp:
    if tag:
        words.append(temp)
    else:
        words.append(temp[::-1])
print(''.join(words))