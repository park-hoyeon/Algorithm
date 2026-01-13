import sys
input = sys.stdin.readline

n = list(input().strip())
n.sort(reverse=True)
print(''.join(n))
