field = [list(map(int, input().split())) for _ in range(9)]

N = len(field)
max_v = 0
max_p = (1, 1)

for i in range(N):
    for j in range(N):
        if field[i][j] > max_v:
            max_v = field[i][j]
            max_p = i+1, j+1
print(max_v)
print(*max_p)
