import sys
n = int(sys.stdin.readline())
store = []
for i in range(n):
    command = sys.stdin.readline().strip()

    if command.startswith("push"):
        answer = command.split()
        store.append(int(answer[1]))

    elif command == "pop":
        if not store: print(-1)
        else: print(store.pop())

    elif command == 'size':
        print(len(store))

    elif command == 'empty':
        if len(store) == 0: print(1)
        else: print(0)

    elif command == 'top':
        if len(store) == 0: print(-1)
        else: print(store[-1])
