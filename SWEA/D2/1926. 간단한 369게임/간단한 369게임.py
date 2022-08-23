N = int(input())

arr = list(range(1, 1 + N))

for num in (range(1, 1 + N)):
    cnt = 0
    for n in str(num):
        if n in '369':
            cnt += 1
    if cnt == 1:
        num = '-'
    elif cnt == 2:
        num = '--'
    elif cnt == 3:
        num = '---'
    else:
        num = str(num)
    print(num, end=' ')
