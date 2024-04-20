def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]: # numbers[i]-1이 인덱스
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer