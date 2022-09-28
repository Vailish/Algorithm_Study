def kills(x, y):
    result = [field[x][y], field[x][y]]  # +, x 모양 잡은 파리 수
    # 0 : +자로 잡는 경우, 1 : x자로 잡는 경우
    for method in range(2):
        for i in range(4):
            nx = x + [[-1, 1, 0, 0], [1, -1, 1, -1]][method][i]  # 1) 상 하 좌 우
            ny = y + [[0, 0, -1, 1], [1, 1, -1, -1]][method][i]  # 2) 우상 우하 좌상 좌하
            cnt = 0

            while 0 <= nx < N and 0 <= ny < N and cnt < M-1:
                cnt += 1
                result[method] += field[nx][ny]
                nx += [[-1, 1, 0, 0], [1, -1, 1, -1]][method][i]
                ny += [[0, 0, -1, 1], [1, 1, -1, -1]][method][i]

    return max(result)


for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    answer = []
    for a in range(N):
        for b in range(N):
            answer.append(kills(a, b))
    print(f'#{case}', max(answer))
