import sys
input = sys.stdin.readline

names = {}
tree_count = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in names:
        names[tree] += 1
    else:
        names[tree] = 1
    tree_count += 1

trees = list(names.keys())
trees.sort()

for i in trees:
    print("%s %.4f" %(i, names[i]/tree_count * 100))