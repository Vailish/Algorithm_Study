idx = [
    '0001101', '0011001',
    '0010011', '0111101',
    '0100011', '0110001',
    '0101111', '0111011',
    '0110111', '0001011']

for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # N = 세로, M = 가로

    # 유효 코드 뽑아내기
    for _ in range(N):
        temp = input()
        if '1' in temp:
            data = temp
    # 필요없는 코드 제거
    end = M -data[::-1].index('1')
    start = end - 56
    data = data[start:end]

    # 암호 해석하기
    result = []
    for num in range(0, 56, 7):
        result.append(idx.index(data[num:num+7]))

    # 코드 검사
    chk = 0
    for n in range(8):
        if n % 2:  # 홀수일때
            chk += result[n]
        else:
            chk += 3 * result[n]
    if chk % 10 == 0:
        print(f'#{case} {sum(result)}')
    else:
        print(f'#{case} 0')
