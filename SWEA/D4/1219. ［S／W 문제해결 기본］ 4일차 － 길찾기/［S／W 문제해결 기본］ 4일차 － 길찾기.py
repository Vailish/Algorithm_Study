def dfs(v):
    visited[v] == 1
    result.append(v)

    for next_v in graph[v]:
        if visited[next_v] == 0:
            dfs(next_v)


for _ in range(10):
    case, m = map(int, input().split())  # case = case 수, m = 경로 수
    edges = list(map(int, input().split()))  # edges = 경로정보
    result = []
    visited = [0] * 100
    graph = [[] for _ in range(100)]

    for i in range(0, len(edges), 2):
        v1, v2 = edges[i], edges[i + 1]
        graph[v1].append(v2)

    dfs(0)
    if 99 in result:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')
