name = input()
arr = []
while True:
    if name in arr:
        print(name + "??!")
        break
    else:
        arr.append(name)