def cc(a, b):
    c = a - b
    if c >= 0:
        return c
    return -c

# 델타이동
dx = [1, 0, -1, 0]  # 우 하 좌 상
dy = [0, 1, 0, -1]  # 우 하 좌 상
direction = [0, 1, 2, 3]

for case in range(1, 11):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    # 델타검색
    cc_sum = 0
    for i in range(N):
        for j in range(N):
            for num in range(4):  # 델타 검색
                if 0 <= i + dy[num] <= N-1 and 0 <= j + dx[num] <= N-1:
                    cc_sum += cc(field[i][j], field[i+dy[num]][j+dx[num]])
    print(f'#{case} {cc_sum}')
