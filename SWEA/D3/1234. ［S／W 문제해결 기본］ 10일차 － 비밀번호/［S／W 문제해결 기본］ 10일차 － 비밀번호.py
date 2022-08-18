for case in range(1, 11):
    N, nums = input().split()  # N = 문자열 길이, nums = 문자열
    N = int(N)
    stack = []
    top = -1

    stack.append(nums[0])
    top += 1

    # 검사
    for i in range(1, N):
        if top == -1:
            top += 1
            stack.append(nums[i])
        elif stack[top] == nums[i]:
            stack.pop()
            top -= 1
        else:
            top += 1
            stack.append(nums[i])
    print(f'#{case} {"".join(stack)}')