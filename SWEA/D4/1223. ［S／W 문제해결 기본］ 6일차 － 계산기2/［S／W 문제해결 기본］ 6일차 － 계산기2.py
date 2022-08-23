for case in range(1, 11):
    length = int(input())
    word = input()
    idx = ''
    stack = []

    for token in word:
        if token in '*/+-()':
            if not stack and token == '(':
                stack.append(token)

            elif token in '*/':
                while stack and stack[-1] in '*/':
                    idx += stack.pop()
                stack.append(token)

            elif token in '+-':
                while stack and stack != '(':
                    idx += stack.pop()
                stack.append(token)

            elif token == ')':
                while stack and stack != '(':
                    idx += stack.pop()
                stack.pop()

        else:
            idx += token

    while stack:
        idx += stack.pop()

    for char in idx:
        if not char in '*/+-':
            stack.append(int(char))

        else:
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

    print(f'#{case} {stack[-1]}')
