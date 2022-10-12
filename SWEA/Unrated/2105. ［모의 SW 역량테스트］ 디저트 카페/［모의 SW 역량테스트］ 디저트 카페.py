dr = [-1, -1, 1, 1]  # 좌상 우상 우하 좌하
dc = [-1, 1, 1, -1]


def dfs(r, c, path, direction):
    global result
    # 종료 조건
    if r == i and c == j and direction == 3 and len(path) > 2:  # 한 칸 이동 후 복귀 경우 제외
        if result < len(path):
            result = len(path)
        return

    # 조건 검색
    if 0 <= r < N and 0 <= c < N and field[r][c] not in path:  # 어차피 방향은 고정되어 있으니 값만 확인
        new_path = path + [field[r][c]]

        # 델타 이동
        nr = r + dr[direction]
        nc = c + dc[direction]

        # 더 전진 할 수 있으면 더 전진
        dfs(nr, nc, new_path, direction)

        # 더 전진 할 수 없다면 방향 변경
        if direction < 3:
            nr = r + dr[direction+1]
            nc = c + dc[direction+1]

            dfs(nr, nc, new_path, direction+1)


for case in range(1, 1 + int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    result = -1  # result = 최대 디저트 값
    for i in range(N):
        for j in range(N):
            dfs(i, j, [], 0)

    print(f'#{case}', result)