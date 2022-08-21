def cc(a, b):
    c = 0
    if a > b:
        c = a - b
    else:
        a < b
        c = b - a
    return c

# 델타이동
dx = [1, 0, -1, 0]  # 우 하 좌 상
dy = [0, 1, 0, -1]  # 우 하 좌 상
direction = [0, 1, 2, 3]

for case in range(1, 11):
    N = int(input())
    # 예외 처리를 위한 리스트 수정
    field = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    field = [[0] * (N+2)] + field + [[0] * (N+2)]
    # 현위치
    x = 1
    y = 1

    # 델타검색
    cc_sum = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for num in range(4):  # 델타 검색
                cc_sum += cc(field[i][j], field[i+dy[num]][j+dx[num]])

    m_sum = 0
    for i in [1, N]:
        for j in range(1, N + 1):
            m_sum += field[i][j] + field[j][i]
    print(f'#{case} {cc_sum - m_sum}')