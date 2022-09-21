# 터널 구조물 정보
idx = {
    '1': [[-1, 1, 0, 0], [0, 0, -1, 1]],  # dx, dy : 상, 하, 좌, 우
    '2': [[-1, 1], [0, 0]],  # 상, 하
    '3': [[0, 0], [-1, 1]],  # 좌, 우
    '4': [[-1, 0], [0, 1]],  # 상, 우
    '5': [[1, 0], [0, 1]],  # 하, 우
    '6': [[1, 0], [0, -1]],  # 하, 좌
    '7': [[-1, 0], [0, -1]]  # 상, 좌
}

def bfs(x, y, t):
    visited[x][y] = 1  # 시작지점 방문처리
    queue = [(x, y, t)]

    while queue:
        x, y, t = queue.pop(0)
        if t == 1:
            break
        # 현 위치 구조물 정보 확인
        [dx, dy] = idx.get(str(field[x][y]))
        # delta search
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            # 기본조건
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and field[nx][ny] != 0:
                # 연결여부 확인
                # idx.get(str(field[nx][ny])여기의 방향이 - 붙은 방향이 있는지 검사
                dx_1, dy_1 = idx.get(str(field[nx][ny]))
                if -dx[i] in dx_1 and -dy[i] in dy_1:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, t - 1))

    # visited의 합 구하기
    result = 0
    for lst in visited:
        result += sum(lst)
    return result


for case in range(1, 1+int(input())):
    N, M, R, C, L = map(int, input().split())  # N = 세로, M = 가로, (R, C) = 시작지점, L = 시간
    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]  # visited : 탈주범이 갈 수 있는 곳
    print(f'#{case} {bfs(R, C, L)}')  # bfs결과 값으로 탈주범이 위치할 수 있는 장소의 개수
