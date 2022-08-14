for _ in range(1, 11):
    case = int(input())
    field = [[0] + list(map(int, input().split())) + [0] for _ in range(100)] # 좌 우에 오류 방지용 0 삽입

    for i in range(102):  # 시작점의 y 구하기
        if field[99][i] == 2:  # field[99].index(2) 로 구해도 됨.
            start_y = i

    x = 99
    y = start_y
    # 사다리 올라가기

    while True:
        if x == 0:  # 도착했을 때
            break
        elif field[x][y-1] == 1 and y != 0:  # 좌로 탐색
            while field[x][y-1] and y != 0:
                y -= 1
            x -= 1
        elif field[x][y+1] == 1 and y != 100:  # 우로 탐색
            while field[x][y+1] and y != 100:
                y += 1
            x -= 1
        else:  # 위로 올라가기
            x -= 1
    print(f'#{case} {y-1}')