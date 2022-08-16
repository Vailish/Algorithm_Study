for _ in range(10):
    case = int(input())
    arr = [input() for _ in range(100)]
    arr_2 = []
    for i in range(100):
        temp = ''
        for j in range(100):
            temp += arr[j][i]
        arr_2.append(temp)

    result = 0
    for i in range(100):
        for num in range(1, 101):  # num = 회문 길이
            for j in range(100 - num + 1):
                word = arr[i][j:j+num]  # 가로 검사
                word_2 = arr_2[i][j:j+num]  # 세로 검사
                if word == word[::-1] or word_2 == word_2[::-1]:
                    if result < num:
                        result = num
                    break
    print(f'#{case} {result}')