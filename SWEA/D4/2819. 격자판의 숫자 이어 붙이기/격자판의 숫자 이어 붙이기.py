# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, d, temp):
    temp += str(arr[x][y])

    if d == 6:
        if len(temp) == 7:
            result.add(temp)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, d + 1, temp)
    return


def solution():
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, '')
    return len(result)


for case in range(1, 1 + int(input())):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    print(f'#{case} {solution()}')
