def solution():
    n = int(input())
    result = [float("inf")] * (n + 1)
    result[0] = 0
    result[1] = 1

    for i in range(2, n + 1):
        j = 1
        while j * j <= i:  # 해당 값보다 작은 제곱수 활용
            # i-j*j은 목표값에 제곱수를 뺀 값의 생성가능 최소값이고 +1은 제곱수 값을 추가한다는뜻
            result[i] = min(result[i], result[i - j * j] + 1)
            j += 1

    print(result[n])

solution()
