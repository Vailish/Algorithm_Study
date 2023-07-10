def solution(grid):
    answer = []
    n, m = len(grid), len(grid[0])
    visited = [[[0 for _ in range(4)] for _ in range(m)] for _ in range(n)]
    directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]  # D, L, U, R

    for r in range(n):
        for c in range(m):
            for d in range(4):
                if not visited[r][c][d]:
                    nr, nc, nd = r, c, d
                    cnt = 0
                    while not visited[nr][nc][nd]:
                        visited[nr][nc][nd] = 1
                        cnt += 1
                        nr, nc = (nr + directions[nd][0]) % n, (nc + directions[nd][1]) % m
                        if grid[nr][nc] == "R":
                            nd = (nd + 1) % 4
                        elif grid[nr][nc] == "L":
                            nd = (nd - 1) % 4
                    answer.append(cnt)
    return sorted(answer)