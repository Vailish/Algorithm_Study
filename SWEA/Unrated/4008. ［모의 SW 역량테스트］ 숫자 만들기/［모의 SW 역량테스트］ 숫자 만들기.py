def dfs(depth, remains, value):
    global max_value, min_value
    # 종료조건
    if remains == [0, 0, 0, 0] or depth == N:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return

    # 선택
    for i in range(4):  # +, -, *, /
        if remains[i] >= 1:
            new_remains = remains[:]
            new_remains[i] -= 1
            if i == 0:
                new_value = value + numbers[depth]
            elif i == 1:
                new_value = value - numbers[depth]
            elif i == 2:
                new_value = value * numbers[depth]
            else:  # i == 3:
                   new_value = int(value / numbers[depth])
            dfs(depth + 1, new_remains, new_value)


for case in range(1, 1 + int(input())):
    N = int(input())
    operator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    max_value = -1000000000
    min_value = 1000000000
    dfs(1, operator, numbers[0])
    print(f'#{case}', max_value - min_value)
