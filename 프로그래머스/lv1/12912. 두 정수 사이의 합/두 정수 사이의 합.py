def solution(a, b):
    a, b = sorted((a, b))
    answer = 0
    for num in range(a, b+1):
        answer += num
    return answer