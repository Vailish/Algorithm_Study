def solution():
    for i in range(N):
        for j in range(N):
            x, y = i, j
            for direction in range(8):
                nx = x + [-1, 1, 0, 0, 1, -1, 1, -1][direction]  # 상 하 좌 우 우상 우하 좌상 좌하
                ny = y + [0, 0, -1, 1, 1, 1, -1, -1][direction]
                cnt = 1
                while 0 <= nx < N and 0 <= ny < N and field[nx][ny] == 'o' and field[x][y] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        return 'YES'
                    nx += [-1, 1, 0, 0, 1, -1, 1, -1][direction]
                    ny += [0, 0, -1, 1, 1, 1, -1, -1][direction]

    return 'NO'


for case in range(1, 1 + int(input())):
    N = int(input())
    field = [list(input()) for _ in range(N)]
    print(f'#{case}', solution())
