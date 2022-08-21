dx = [-1, 0, 1, 0]  # 상 우 하 좌
dy = [0, 1, 0, -1]  # 상 우 하 좌
direction = 0

C, R = map(int, input().split())  # 공연장 크기 C = 가로, R = 세로
stage = [[0]*C for _ in range(R)]
K = int(input())

# 현재 위치
x, y = R - 1, 0
result = 0, 0

# 채워넣기
for i in range(1, C * R + 1):
    stage[x][y] = i

    if i == K:
        result = y + 1, R - x
        break

    # 자리 이동
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 검사
    if 0 <= nx < R and 0 <= ny < C and stage[nx][ny] == 0:
        x = nx
        y = ny
    else:
        direction = (direction + 1) % 4
        x = x + dx[direction]
        y = y + dy[direction]

if K > C * R:
    print(0)
else:
    print(*result)