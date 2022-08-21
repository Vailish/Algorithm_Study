N, M = map(int, input().split())
chess_idx = list(input() for _ in range(N))
chess_ansW = []
chess_ansB = []
for num in range(8):
    if num % 2 == 0:
        chess_ansW.append('WBWBWBWB')
        chess_ansB.append('BWBWBWBW')
    else:
        chess_ansW.append('BWBWBWBW')
        chess_ansB.append('WBWBWBWB')

cnt_W = 0
cnt_B = 0
min_W = 64
min_B = 64
for i in range(N-7):
    for j in range(M-7):
        for a in range(8):
            for b in range(8):
                if chess_idx[a+i][b+j] != chess_ansB[a][b]:
                    cnt_B += 1
                if chess_idx[a+i][b+j] != chess_ansW[a][b]:
                    cnt_W += 1
        if min_B > cnt_B:
            min_B = cnt_B
        if min_W > cnt_W:
            min_W = cnt_W
        cnt_B = 0
        cnt_W = 0
if min_B > min_W:
    print(min_W)
else:
    print(min_B)
