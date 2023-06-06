def solution(record):
    users = {}
    answer = []
    # 제일 뒤에 Change 혹은 Enter로 등장한 uid의 닉네임을 정한다.
    for i in range(len(record)):
        tmp = list(record[i].split())
        if tmp[0] == "Enter" or tmp[0] == "Change":
            users[tmp[1]] = tmp[2]

    # 정한 닉네임을 바탕으로 결과를 출력한다.
    for i in range(len(record)):
        tmp = list(record[i].split())
        if tmp[0] == "Enter":
            answer.append(f'{users[tmp[1]]}님이 들어왔습니다.')
        elif tmp[0] == "Leave":
            answer.append(f'{users[tmp[1]]}님이 나갔습니다.')
            
    return answer