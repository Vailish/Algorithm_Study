T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split(" "))

    grade = ("A+", "A0", "A-", "B+", "B0", "B-","C+", "C0", "C-", "D0")

    scoreList = []
    for n in range(1, N+1):
        score = list(map(int, input().split()))
        score[0] = score[0] * 0.35
        score[1] = score[1] * 0.45
        score[2] = score[2] * 0.20
        scoreList.append(sum(score))

    a = scoreList.copy()
    a.sort(reverse=True)

    print("#{} {}".format(i, grade[int(a.index(scoreList[K-1])/(N/10))]))