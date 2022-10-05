def solution():
    clients.sort()
    cnt_clients = [0] * (11111 + 1)
    for i in clients:
        cnt_clients[i] += 1

    # 오픈과 동시에 온 사람일 경우 무조건 기다려야 함
    if cnt_clients[0] != 0:
        return 'Impossible'

    bread = 0
    time = 0
    while time < clients[-1]:
        time += 1

        if time % M == 0:
            bread += K

        if cnt_clients[time] != 0:
            if bread < cnt_clients[time]:
                return 'Impossible'
            else:
                bread -= cnt_clients[time]

    return 'Possible'


for case in range(1, 1 + int(input())):
    N, M, K = map(int, input().split())
    clients = list(map(int, input().split()))
    print(f'#{case}', solution())
