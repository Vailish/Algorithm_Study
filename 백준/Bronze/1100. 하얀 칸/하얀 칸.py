chess = [input() for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and chess[i][j] == 'F':  # i, j가 2의 배수일 때
            cnt += 1
        if i % 2 == 1 and j % 2 == 1 and chess[i][j] == 'F':  # i, j가 홀 수 일 때
            cnt += 1
print(cnt)