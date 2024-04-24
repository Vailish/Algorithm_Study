def solution(today, terms, privacies):
    answer = []
    term_dict = dict()
    for term in terms:
        v1, v2 = term.split(" ");
        term_dict[v1] = int(v2)
    # 오늘날짜 - 개인정보 수집일자 > 0 -> answer.append
    for i in range(len(privacies)):
        if compare_date(today, privacies[i]) >= term_dict[privacies[i][-1]] * 28:
            answer.append(i+1)
    
    return answer

def compare_date(today, privacy):
    t_days = int(today[2:4]) * 12 * 28 + int(today[5:7]) * 28 + int(today[8:10])
    c_days = int(privacy[2:4]) * 12 * 28 + int(privacy[5:7]) * 28 + int(privacy[8:10])
    return t_days - c_days
