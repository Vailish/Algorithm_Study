def play(cmd, x, y):
    nx = x
    ny = y
    if cmd == 'U':
        nx -= 1
        if 0 <= nx < H and field[nx][ny] == '.':
            field[x][y] = '.'
            field[nx][ny] = '^'
            return nx, ny
        else:
            field[x][y] = '^'
            return x, y

    elif cmd == 'D':
        nx += 1
        if 0 <= nx < H and field[nx][ny] == '.':
            field[x][y] = '.'
            field[nx][ny] = 'v'
            return nx, ny
        else:
            field[x][y] = 'v'
            return x, y

    elif cmd == 'L':
        ny -= 1
        if 0 <= ny < W and field[nx][ny] == '.':
            field[x][y] = '.'
            field[nx][ny] = '<'
            return nx, ny
        else:
            field[x][y] = '<'
            return x, y

    elif cmd == 'R':
        ny += 1
        if 0 <= nx < H and 0 <= ny < W and field[nx][ny] == '.':
            field[x][y] = '.'
            field[nx][ny] = '>'
            return nx, ny
        else:
            field[x][y] = '>'
            return x, y

    elif cmd == 'S':
        if field[x][y] == '^':
            while 0 <= nx < H and field[nx][ny] != '*' and field[nx][ny] != '#':
                nx -= 1
            if 0 <= nx < H and field[nx][ny] == '*':
                field[nx][ny] = '.'
            return x, y

        elif field[x][y] == 'v':
            while 0 <= nx < H and field[nx][ny] != '*' and field[nx][ny] != '#':
                nx += 1
            if 0 <= nx < H and field[nx][ny] == '*':
                field[nx][ny] = '.'
            return x, y

        elif field[x][y] == '<':
            while 0 <= ny < W and field[nx][ny] != '*' and field[nx][ny] != '#':
                ny -= 1
            if 0 <= ny < W and field[nx][ny] == '*':
                field[nx][ny] = '.'
            return x, y

        elif field[x][y] == '>':
            while 0 <= ny < W and field[nx][ny] != '*' and field[nx][ny] != '#':
                ny += 1
            if 0 <= ny < W and field[nx][ny] == '*':
                field[nx][ny] = '.'
            return x, y

    return x, y


for case in range(1, 1 + int(input())):
    H, W = map(int, input().split())  # H = 높이, W = 너비
    field = [list(input()) for _ in range(H)]
    N = int(input())  # 명령어 길이
    commands = input()

    # 현재 위치 찾기
    i, j = -1, -1  # x, y = 탱크의 시작위치
    for n in range(H):
        for m in range(W):
            if field[n][m] in '<>^v':
                i, j = n, m


    for command in commands:
        i, j = play(command, i, j)

    print(f'#{case}', end=' ')
    for lst in field:
        print(''.join(lst))
