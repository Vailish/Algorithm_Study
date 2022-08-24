def solution(n):
    answer = ''
    
    for num in range(n):
        if num % 2:
            answer += '박'
        else:
            answer += '수'
        
    return answer