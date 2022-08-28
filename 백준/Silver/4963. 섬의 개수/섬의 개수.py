import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    visited[x][y] = True
    cnt = 1

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and field[nx][ny]:
            cnt = 1
            dfs(nx, ny)

    return cnt


dx = [0, 1, 0, -1, 1, 1, -1, -1]  # 우 하 좌 상 대각1, 대각2, 대각3, 대각4
dy = [1, 0, -1, 0, 1, -1, -1, 1]  # 우 하 좌 상 대각1, 대각2, 대각3, 대각4

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    else:
        field = [list(map(int, input().split())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]
        result = []

        for i in range(h):
            for j in range(w):
                if not visited[i][j] and field[i][j]:
                    result.append(dfs(i, j))
        print(result.count(1))
