end_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 매 달의 끝


def calculator(data):
    lst = list(map(int, data.split()))
    for num in range(1, int(len(lst) / 4 + 1)):
        # 계산할 각 월과 일을 저장
        m_1 = lst[4 * num - 4]
        d_1 = lst[4 * num - 3]
        m_2 = lst[4 * num - 2]
        d_2 = lst[4 * num - 1]

        # 조건에 맞게 계산하기
        # m_1 월 ~ m_2 월 - d_1일 + d_2일
        result = sum(end_day[m_1: m_2]) - d_1 + d_2 + 1
        return result


for case in range(1, 1 + int(input())):
    print(f'#{case} {calculator(input())}')
