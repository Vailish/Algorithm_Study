def solution(time):
    meeting_time = sorted(time, key=lambda x: (x[1], x[0]))

    result = [meeting_time[0]]
    for t in meeting_time[1:]:
        if result[len(result)-1][1] <= t[0]:
            result.append(t)
    return len(result)


N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
print(solution(time))
