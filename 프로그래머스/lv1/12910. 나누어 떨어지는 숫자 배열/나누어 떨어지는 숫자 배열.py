def solution(arr, divisor):
    answer = []
    for num in sorted(arr):
        if not num % divisor:
            answer.append(num)
    if not answer:
        answer = [-1]
    return answer