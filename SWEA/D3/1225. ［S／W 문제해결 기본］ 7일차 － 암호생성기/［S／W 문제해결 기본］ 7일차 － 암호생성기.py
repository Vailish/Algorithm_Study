for _ in range(1, 11):
    case = int(input())
    queue = list(map(int, input().split()))
    
    stop = False  # while 문 탈출 조건

    while not stop:
        for num in range(1, 6):  # 1 ~ 5까지 바퀴마다 빼준다
            if queue[0] - num <= 0:  # 0 이하로 내려가면 0을 붙이고 탈출한다
                queue.pop(0)
                queue.append(0)
                stop = True
                break
            queue.append(queue.pop(0) - num)
    print(f'#{case}', *queue)