from collections import deque


def solution(maps):
    dq = deque()
    dq.append((0, 0, 1))
    m = len(maps[0])
    n = len(maps)
    visited = [[0] * m for _ in range(n)]
    
    while dq:
        r, c, d = dq.popleft()
        visited[r][c] = 1

        # 이동변수 상, 하, 좌, 우
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        # 델타이동
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] and not visited[nr][nc]:
                # 목표에 도달했다면, 거리를 반환
                if (nr, nc) == (n - 1, m - 1):
                    return d + 1
                # 아니라면, dq에 추가 하고 못지나가게 벽처리
                maps[nr][nc] = 0
                dq.append((nr, nc, d + 1))
    return -1