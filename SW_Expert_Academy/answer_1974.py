T = int(input())

for t in range(1, T+1) :
    test_case = [ [0]*9 for _ in range(9) ]
    for i in range(9) :
        test_case[i] = list(map(int, input().split()))

    # 3x3 격자
    res1 = 1
    for i in range(0, 9, 3) :
        for j in range(0, 9, 3) :
            test = {}
            test_case1 = []
            for k in range(3) :
                for l in range(3) :
                    test_case1 += [test_case[k+i][l+j]]
            for k in range(1, 10) :
                test[k] = test_case1.count(k)
            if 0 in test.values() :
                res1 = res1*0
            else :
                res1 = res1*1
    # 가로줄
    res2 = 1
    for i in range(9) :
        test = {}
        for j in range(1, 10) :
            test[j] = test_case[i].count(j)
        if 0 in test.values() :
            res2 = res2*0
        else :
            res2 = res2*1
    # 세로줄
    res3 = 1
    for i in range(9) :
        test = {}
        test_case2 = []
        for j in range(9) :
            test_case2 += [test_case[j][i]]
        for j in range(1, 10) :
            test[j] = test_case2.count(j)
        if 0 in test.values() :
            res3 = res3*0
        else :
            res3 = res3*1

    result = res1 * res2 * res3
    print("#{} {}".format(t, result))