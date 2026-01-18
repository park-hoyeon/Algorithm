import sys
input = sys.stdin.readline

w = int(input())

for i in range(w):
    words = input().strip().split()
    print("Case #%d:" %(i+1), " ".join(words[::-1]))