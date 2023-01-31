from collections import Counter


def solution(weights):
    answer = 0
    
    # 1:1 처리
    for k, v in Counter(weights).items():
        if v > 1:
            answer += v * (v - 1) // 2
    
    # 1 : 1/2 3/4 3/2 처리
    for weight in set(weights):
        for rate in [1/2, 3/4, 3/2]:
            if weight * rate in weights:
                answer += weights.count(weight) * weights.count(weight * rate)
    
    
    return answer