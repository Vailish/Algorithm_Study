dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0 , -1, 1, 1, 1, -1, -1]


def search(x, y, c):
    field[x][y] = c
    path = []

    # delta search
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and field[nx][ny] == -c:
            while True:
                path.append((nx, ny))
                if 0 <= nx < N and 0 <= ny < N and field[nx][ny] == -c:
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                elif 0 <= nx < N and 0 <= ny < N and field[nx][ny] == c:
                    break
                else:
                    path = []
                    break
            # 조건 맞는 곳 칠해주기
            for k, l in path:
                field[k][l] = c


def solution():
    # 게임 돌리기
    for data in game:
        y, x, c = data  # 2,3 ->(뒤집기) 3, 2 ->(-1) 2, 1 //
        if c == 2:
            c = -1
        search(x-1, y-1, c)
    cnt = [0, 0]  # (cnt_balck, cnt_white)

    # 돌 세기
    for lst in field:
        cnt[0] += lst.count(1)
        cnt[1] += lst.count(-1)

    return f'{cnt[0]} {cnt[1]}'


for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # N = 한 변의 길이, M = 돌 놓는 횟수(턴)
    game = [list(map(int, input().split())) for _ in range(M)]  # [(x, y, c)] x, y에 c색 돌 놓기
    field = [[0]*N for _ in range(N)]

    # 필드 채워 넣기(시작상태 설정)
    field[N//2-1][N//2-1] = -1
    field[N // 2 - 1][N // 2] = 1
    field[N // 2][N // 2 - 1] = 1
    field[N // 2][N // 2] = -1

    print(f'#{case} {solution()}')
