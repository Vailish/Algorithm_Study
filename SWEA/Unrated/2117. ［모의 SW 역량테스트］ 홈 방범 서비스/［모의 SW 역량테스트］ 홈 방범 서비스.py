# 확산모양!! bfs!!
dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]


def bfs(x, y, k):
    values = []  # 조건에 맞는 집들의 수
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    queue = [(x, y, k)]
    cnt = field[x][y]  # 범위에 들어간 집의 좌표들
    ex_k = 0  # 확산 단계 변화에 맞춰 비교하기 위한 값
    while queue:
        x, y, k = queue.pop(0)
        if ex_k + 1 == k:
            ex_k += 1
            # 조건에 맞다면
            if cnt * M >= k**2 + (k-1)**2:
                values.append(cnt)

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, k+1))
                if field[nx][ny] == 1:
                    cnt += 1

    return max(values) if values else 0


def solution():
    result = []
    for i in range(N):
        for j in range(N):
            result.append(bfs(i, j, 1))
    return max(result)


for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # N = 도시의 크기, M = 집 하나당 지불비용
    field = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{case}', solution())
