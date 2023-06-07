import heapq


def solution():
    heap = []
    for _ in range(int(input())):
        heap.append(int(input()))
    heapq.heapify(heap)
    while heap:
        print(heapq.heappop(heap))


solution()
