from heapq import heappush, heappop


def solution(n, k, enemy):
    # 힙 안으로 넣어서 k번 이후부터 제일 작은 수들만 병사 값에서 빼주면 됨!
    heap = []
    for idx in range(len(enemy)):
        heappush(heap, enemy[idx])
        if idx + 1 > k:
            n -= heappop(heap)
        if n < 0:
            return idx
    return len(enemy)