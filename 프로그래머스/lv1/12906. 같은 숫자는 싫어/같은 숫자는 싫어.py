def solution(arr):
    answer = [arr[0]]
    for num in range(1, len(arr)):
        if arr[num-1] != arr[num]:
            answer.append(arr[num])
    return answer