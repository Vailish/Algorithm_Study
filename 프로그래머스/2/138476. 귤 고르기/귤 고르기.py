def solution(k, tangerine):
    answer = 0
    # k개를 골라 판매
    # 최대한 같은 종류로 하장~
    cnt_dict = dict()
    for t in tangerine:
        if t in cnt_dict:
            cnt_dict[t] += 1
            if cnt_dict[t] >= k:
                return 1
        else:
            cnt_dict[t] = 1
    cnt = 0
    tmp = 0
    for n in sorted(list(cnt_dict.values()), reverse=True):
        cnt += 1
        tmp += n
        if tmp >= k:
            return cnt
    return answer