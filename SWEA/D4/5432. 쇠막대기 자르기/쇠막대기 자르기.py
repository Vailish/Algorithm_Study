for case in range(1, 1 + int(input())):
    shape = input()
    stick = 0  # 현 위치에 겹친 쇠막대의 개수
    result = 0  # 잘린 쇠막대의 총 개수
    shape = shape.replace('()', '!')  # 편의상 문자 하나로 변경

    # 앞에서 부터 그려나가기
    for command in shape:
        if command == '(':
            stick += 1
        elif command == ')':
            result += 1
            stick -= 1
        else:  # !의 경우
            result += stick
    print(f'#{case} {result}')