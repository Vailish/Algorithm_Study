N = int(input())
target_n = int(input())
target_p = (0, 0)

dx = [1, 0, -1, 0]  # 하 우 상 좌
dy = [0, 1, 0, -1]  # 하 우 상 좌
direction = 0

# 현 위치
x, y = 0, 0
snail = [[0]*N for _ in range(N)]

# 달팽이 질주!
for i in range(N**2, 0, -1):
    snail[x][y] = i

    # 필요한 값 저장
    if i == target_n:
        target_p = x + 1, y + 1

    # 위치 이동
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 발판 검사
    if 0 <= nx < N and 0 <= ny < N and snail[x+dx[direction]][y+dy[direction]] == 0:
        x = nx
        y = ny
    else:
        direction = (direction + 1) % 4
        x = x + dx[direction]
        y = y + dy[direction]

for graph in snail:
    print(*graph)
print(*target_p)
