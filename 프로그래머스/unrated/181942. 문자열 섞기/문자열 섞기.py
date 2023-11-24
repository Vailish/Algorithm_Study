def solution(str1, str2):
    answer = ''
    a = list(str1)
    b = list(str2)
    n = 0
    for _ in range(len(a) * 2):
        if n % 2:
            answer += b.pop(0)
        else:
            answer += a.pop(0)
        n += 1
    return answer
