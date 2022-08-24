def dfs(x, y):
    global total
    visited[x][y] = True
    total += 1  # 함수를 부를때마다(이동시마다 == 집이 있을 때 마다)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny]:
            dfs(nx, ny)


N = int(input())
arr = [list(int(num) for num in input()) for _ in range(N)]
# arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [0, 1, 0, -1]  # 우 하 좌 상
dy = [1, 0, -1, 0]  # 우 하 좌 상
result = []

for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] == 1:
            total = 0
            dfs(i, j)
            result.append(total)

print(len(result))
for idx in sorted(result):
    print(idx)
