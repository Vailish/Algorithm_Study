def isValid(row, col):
    if (row >= 0 and row < n and col >= 0 and col < n):
        return True
    else:
        return False

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    snail = [[0]*n for _ in range(n)]

    # rd: row of direction, cd: column of direction
    # right, down, left, up
    rd = [0, 1, 0, -1]
    cd = [1, 0, -1, 0]

    # cr: current row, cc: current column
    cr, cc = 0, -1
    direction = 0 # 0:right, 1:down, 2:left, 3:up

    i = 1
    while (i <= n*n):
        cr += rd[direction]
        cc += cd[direction]

        while(isValid(cr, cc) and snail[cr][cc] == 0):
            snail[cr][cc] = i
            cr += rd[direction]
            cc += cd[direction]
            i += 1

        # 범위를 벗어났으므로 진행된 방향 반대로 한칸 이동(이동하기 전으로 다시 돌아감)
        cr -= rd[direction]
        cc -= cd[direction]

        # 다음 방향으로 넘어가는데, 우-하-좌-상 4가지 방향으로 반복해서 순환되므로 % 연산 사용
        direction = (direction + 1) % 4

    print(f'#{test_case}')
    for row in snail:
        print(*row) # *붙이면 [] 없이 출력