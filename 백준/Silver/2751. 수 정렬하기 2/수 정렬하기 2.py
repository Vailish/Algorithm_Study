import heapq


def solution():
    heap = []
    for _ in range(int(input())):
        heapq.heappush(heap, int(input()))
    while heap:
        print(heapq.heappop(heap))


solution()
