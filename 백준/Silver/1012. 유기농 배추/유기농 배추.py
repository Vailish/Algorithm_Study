import sys
# sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)

def dfs(x, y):
    visited[x][y] = True

    # 델타 검색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and ground[nx][ny]:
            dfs(nx, ny)


T = int(input())

dx = [0, 1, 0, -1]  # 우 하 좌 상
dy = [1, 0, -1, 0]  # 우 하 좌 상

for case in range(T):
    M, N, K = map(int, input().split())  # M = 가로, N = 세로, K = 배추 수
    visited = [[False] * M for _ in range(N)]
    ground = [[0] * M for _ in range(N)]
    location = [list(map(int, input().split())) for _ in range(K)]  # 배추 위치
    cnt = 0

    # ground에 배추 채우기
    for j, i in location:  # N, M
        ground[i][j] = 1

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and ground[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)
