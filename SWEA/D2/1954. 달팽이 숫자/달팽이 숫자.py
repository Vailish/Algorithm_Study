T = int(input())
dx = [0, 1, 0, -1]  # 우, 하, 좌, 상 # 방향 꼭꼭 확인하자
dy = [1, 0, -1, 0]  # 우, 하, 좌, 상

for t in range(1, T+1):
    N = int(input())
    field = [[0]*N for _ in range(N)]
    x, y = 0, 0  # 달팽이 현재 위치
    dir = 0 # 우0, 하1, 좌2, 상3

    # 달팽이전진
    for num in range(1, N**2 + 1): # 숫자찍기
        field[x][y] = num

        # 달팽이 이동할 장소 nx, ny
        nx = x + dx[dir%4]
        ny = y + dy[dir%4]
        
        # 이동 가능 여부 검사
        if 0 <= nx < N and 0 <= ny < N and field[nx][ny] == 0:
            x = nx  #실제로 이동
            y = ny
        else:  # 못가니까 머리를 돌려놔주자
            dir = (dir + 1) % 4
            x += dx[dir]
            y += dy[dir]
    
    # 완주!! 출력!
    print(f'#{t}')
    for lst in field:
        print(*lst)