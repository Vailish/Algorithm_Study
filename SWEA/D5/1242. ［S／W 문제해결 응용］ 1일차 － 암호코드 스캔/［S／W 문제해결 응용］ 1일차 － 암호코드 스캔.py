idx = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}


def solution():
    for line in arr:
        if line == "":  # 비어있으면
            continue
        # 이진수로 바꾸기
        binary_line = ''
        # 이렇게 하면 사라지는 0을 붙여줄 필요가 없음
        binary_line += format(int(line, 16), 'b')

        # 비율 비교하기
        idx_cnt = [0] * 3
        codes = []  # 완성된 코드
        for bin_num in binary_line:
            if idx_cnt[1] == 0 and bin_num == '1':
                idx_cnt[0] += 1
            elif idx_cnt[0] != 0 and idx_cnt[2] == 0 and bin_num == '0':
                idx_cnt[1] += 1
            elif idx_cnt[1] != 0 and bin_num == '1':
                idx_cnt[2] += 1
            elif idx_cnt[2] != 0:
                min_cnt = min(idx_cnt)
                codes.append(idx[(idx_cnt[0]//min_cnt, idx_cnt[1]//min_cnt, idx_cnt[2]//min_cnt)])
            # 초기화 후 이어서 코드 찾기
                idx_cnt = [0] * 3


        # 올바른 코드인지 확인
        for num in range(0, len(codes), 8):
            tmp = 0
            # 중복제거
            if codes[num: num+8] in secret_codes:
                continue
            for n in range(7):
                if n % 2:  # 나머지가 1이다 == 1, 3 == 짝수번
                    tmp += codes[num+n]
                else:
                    tmp += codes[num+n] * 3
            if (tmp + codes[num+7]) % 10 == 0:
                secret_codes.append(codes[num: num+8])

    result = 0
    for temp in secret_codes:
        result += sum(temp)
    return result


for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # N = 세로, M = 가로
    arr = list(set(input().strip().lstrip('0') for _ in range(N)))  # 중복 제거후 리스트로 저장
    secret_codes = []
    print(f'#{case} {solution()}')