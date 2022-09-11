def solution(data):
    commands = data
    speed = 0  # 현재 속도
    distance = 0  # 총 이동 거리
    for command, spd in commands:
        # 0의 경우에는 그냥 속도 그대로 더해주면 됨
        if command == 1:
            speed += spd
        elif command == 2:
            speed -= spd
            if speed < 0:
                speed = 0
        distance += speed
    return distance


for case in range(1, 1 + int(input())):
    queue = []
    for _ in range(int(input())):
        value = list(map(int,input().split()))
        if value == [0]:  # 인덱스 오류 제거용
            queue.append([0, 0])
        else:
            queue.append(value)
    print(f'#{case} {solution(queue)}')
