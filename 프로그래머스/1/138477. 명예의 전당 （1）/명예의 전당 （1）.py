def solution(k, score):
    tmp = []
    for i in range(k):
        tmp.append(score[i])
    answer = [min(tmp)]*k
    
    for i in range(k, len(score)):
        tmp.append(score[i])
        tmp.remove(min(tmp))
        answer.append(min(tmp))
    return answer

def solution(k, score):
    answer = []
    rank = []
    for i in score:
        rank.append(i)
        rank.sort(reverse=True)
        if len(rank)>k:
            del rank[-1]
        answer.append(rank[-1])
    return answer