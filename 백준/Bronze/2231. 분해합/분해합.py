def solution():
    nums = int(input())
    answer = []
    for num in range(nums, 0, -1):  # 여기서 198이라면
        tmp = num
        target_num = str(num)       # target_num == "198"
        for i in range(len(str(num)) -1, -1, -1):
            tmp += int(target_num[i])
        if tmp == nums:
            answer.append(num)
    return answer[-1] if answer else 0


print(solution())
