for case in range(1, 1 + int(input())):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    total = 0
    total2 = 0
    total3 = 0
    temp = []

    for idx in sudoku:
        total += len(set(idx))

    for idx in list(zip(*sudoku)):
        total2 += len(set(idx))

    for i in range(3):
        for j in range(3):
            for a in range(3*i,3*i+3):
                for b in range(3*j,3*j+3):
                    temp.append(sudoku[a][b])
            total3 += len(set(temp))

    if total == 81 and total2 == 81 and total3 == 81:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')