def solution(nums):
    ponketmon = nums[:]
    n = len(ponketmon)/2
    answer = 0
    if len(set(ponketmon)) >= n:
        return n
    else:
        return len(set(ponketmon))