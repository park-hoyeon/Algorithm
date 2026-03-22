import heapq
n,m = map(int, input().split())
card = list(map(int, input().split()))
heap = []
for i in card:
    heapq.heappush(heap, i)

while m > 0:
    new1 = heapq.heappop(heap)
    new2 = heapq.heappop(heap)
    new_num = new1 + new2

    heapq.heappush(heap, new_num)
    heapq.heappush(heap, new_num)
    m -= 1

print(sum(heap))
