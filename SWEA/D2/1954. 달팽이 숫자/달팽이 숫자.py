def dfs(x, y):
    global cnt, direction
    cnt += 1
    visited[x][y] = 1
    field[x][y] = cnt

    if field[x][y] == N**2:
        return
    # 델타이동
    nx = x + [0, 1, 0, -1][direction] # 우, 하, 좌, 상
    ny = y + [1, 0, -1, 0][direction]

    if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] != 1 and field[nx][ny] == 0:
        dfs(nx, ny)
    else:
        direction = (direction + 1) % 4
        nx = x + [0, 1, 0, -1][direction]
        ny = y + [1, 0, -1, 0][direction]
        dfs(nx, ny)
    return


for case in range(1, 1 + int(input())):
    N = int(input())
    field = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    direction = 0
    dfs(0, 0)

    print(f'#{case}')
    for lst in field:
        print(*lst)
