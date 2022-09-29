import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, min_node = heappop(heap)

        if min_dist > distance[min_node]:
            continue

        for next_node, dist in graph[min_node]:
            new_dist = min_dist + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


V, E = map(int, input().split())  # V = 정점의 수, E = 간선의 수
K = int(input())  # 시작 정점
INF = 1000000
distance = [INF] * (V + 1)
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())  # u -> v (w 가중치)
    graph[u].append((v, w))

dijkstra(K)
for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
