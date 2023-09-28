def solution():
    n = int(input())
    stack = []
    answer = []
    cur = 1

    for _ in range(n):
        target_num = int(input())

        while cur <= target_num:
            stack.append(cur)
            answer.append("+")
            cur += 1

        if stack[-1] == target_num:
            stack.pop()
            answer.append("-")
        else:
            print("NO")
            return

    for i in range(len(answer)):
        print(answer[i])

    return


solution()