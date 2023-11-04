def solution():
    answer = 10 ** 10

    def dfs(num, cnt):
        nonlocal answer

        if cnt >= answer:
            return

        if num == 1:
            if answer > cnt:
                answer = cnt
            return

        if num % 3 == 0:
            dfs(num / 3, cnt + 1)
        if num % 2 == 0:
            dfs(num / 2, cnt + 1)
        dfs(num - 1, cnt + 1)

    dfs(int(input()), 0)
    print(answer)


solution()
