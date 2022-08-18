def dfs(v):
    visited[v] = 1

    for next_v in graph[v]:
        if not visited[next_v]:
            global total
            total += 1
            dfs(next_v)


n = int(input())  # n = 정점
m = int(input())  # m = 간선 개수
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
total = 0

for _ in range(m):  # edges
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(1)
print(total)