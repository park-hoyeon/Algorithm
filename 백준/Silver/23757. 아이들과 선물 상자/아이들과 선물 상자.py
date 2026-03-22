import heapq

n,m = map(int, input().split())
gift_count = list(map(int, input().split()))
want = list(map(int, input().split()))

gift_count = [-x for x in gift_count]
heapq.heapify(gift_count)

for i in want:
    if -gift_count[0] < i:
        print(0)
        exit()

    top = -heapq.heappop(gift_count)
    heapq.heappush(gift_count, -(top-i))

print(1)