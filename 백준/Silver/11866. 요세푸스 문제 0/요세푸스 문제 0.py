def solution():
    N, K = map(int, input().split())
    lst = [i for i in range(1, N + 1)]
    answer = []

    while lst:
        for _ in range(K-1):
            lst.append(lst.pop(0))

        answer.append(lst.pop(0))

    result = "<" + str(answer[0])
    for n in answer[1:]:
        result += ", " + str(n)
    result += ">"
    return result

print(solution())