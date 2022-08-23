for case in range(1, 11):
    # 후위 표기식으로 변경
    length = int(input())
    word = input()
    stack = []
    idx = ''

    for token in word:
        if token in '*/+-()':
            if not stack or token == '(':
                stack.append(token)

            elif token in '*/':
                while stack and stack[-1] in '*/':
                    idx += stack.pop()
                stack.append(token)

            elif token in '+-':
                while stack and stack[-1] != '(':
                    idx += stack.pop()
                stack.append(token)

            elif token == ')':
                while stack and stack[-1] != '(':
                    idx += stack.pop()
                # print(stack, idx, sep='#')
                stack.pop()

        else:
            idx += token
    while stack:
        idx += stack.pop()

    # 계산
    for char in idx:
        if char in '*/+-':
            x = stack.pop()
            y = stack.pop()
            if char == '*':
                stack.append(y * x)
            elif char == '/':
                stack.append(y / x)
            elif char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
        else:
            stack.append(int(char))
    print(f'#{case} {stack[-1]}')
