def solution(s):
    answer = []
    my_dict = dict()
    keys = []
    for i in range(len(s)):
        if s[i] not in keys:
            keys.append(s[i])
            my_dict[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - my_dict[s[i]])
            my_dict[s[i]] = i
    return answer