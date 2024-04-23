def solution(sequence, k):
    answer = []
    sum_value = 0
    left, right = 0, -1
    
    while True:
        if sum_value < k:
            right += 1
            if right >= len(sequence):
                break
            sum_value += sequence[right]
        else:
            sum_value -= sequence[left]
            left += 1
            if left >= len(sequence):
                break
        if sum_value == k:
            answer.append([left, right])
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]