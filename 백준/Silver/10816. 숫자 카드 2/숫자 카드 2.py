n = int(input())
card = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

count = {}
card.sort()
for i in card:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

def binary_search(arr,target,start,end):
    if start > end:
        return 0
    mid = (start + end) // 2

    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,end)
    else:
        return binary_search(arr, target, start, mid-1)

for j in find:
    print(binary_search(card,j,0,len(card)-1), end=" ")