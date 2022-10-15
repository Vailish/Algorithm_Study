for _ in range(int(input())):
    lst = input()
    cnt = 1 if lst[0] == 'O' else 0
    result = cnt
    for n in range(1, len(lst)):
        if lst[n] == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)
