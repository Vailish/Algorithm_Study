def solution(n):
    global max_value
    if n == chance:
        tmp = int(''.join(numbers))
        if max_value < tmp:
            max_value = tmp

    else:  # 재귀
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                temp = int(''.join(numbers))
                if (n, temp) not in check:
                    check.add((n, temp))
                    solution(n+1)
                # 확인 다 했으면 원복
                numbers[i], numbers[j] = numbers[j], numbers[i]


for case in range(1, 1 + int(input())):
    numbers, chance = input().split()
    numbers = list(numbers)
    chance = int(chance)
    check = set()  # 중복 확인
    max_value = 0
    solution(0)
    print(f'#{case}', max_value)
