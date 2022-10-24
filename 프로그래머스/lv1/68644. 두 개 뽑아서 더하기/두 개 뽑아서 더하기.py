def solution(numbers):
    result = []
    n = len(numbers)
    for i in range(n-1):
        for j in range(i+1, n):
            num = numbers[i] + numbers[j]
            if num not in result:
                result.append(num)
    result.sort()
    return result