import sys
sys.setrecursionlimit(10000)

def solution(maps):
    answer = []
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    food = 0

    # dfs써서 모든 값 더해서 오름차순으로 정렬해서 반환
    def dfs(r, c):
        nonlocal food
        visited[r][c] = True
        food += int(maps[r][c])
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # 하 우 상 좌
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]) and not visited[nr][nc] and maps[nr][nc] != "X":
                dfs(nr, nc)
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            food = 0
            if not visited[i][j] and maps[i][j] != "X":
                dfs(i,j)
                if food != 0:
                    answer.append(food)
    return sorted(answer) if len(answer) != 0 else [-1]