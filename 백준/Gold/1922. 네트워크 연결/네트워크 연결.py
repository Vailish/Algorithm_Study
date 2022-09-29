def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


N = int(input())  # N = 컴퓨터의 수
M = int(input())  # M = 연결할 수 있는 선의 수
edges = [list(map(int, input().split())) for _ in range(M)]
edges = sorted(edges, key=lambda x: (x[2], x[0], x[1]))
parent = list(range(N+1))
counts = 0
cost = 0

for x, y, dist in edges:
    x_root, y_root = find_set(x), find_set(y)
    if x_root != y_root:
        parent[y_root] = x_root
        cost += dist
        counts += 1
        if counts >= N - 1:
            break
print(cost)
