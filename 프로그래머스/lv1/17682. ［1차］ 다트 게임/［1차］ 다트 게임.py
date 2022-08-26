def solution(dartResult):
    stack = []
    signal = True
    for num in range(len(dartResult)):
        if not signal:
            signal = True
        elif dartResult[num] == '1' and dartResult[num+1] == '0':
            stack.append(10)
            signal = False
        else:
            if dartResult[num] in '0123456789':
                stack.append(int(dartResult[num]))
            elif dartResult[num] in 'SDT':
                if dartResult[num] == 'S':
                    pass
                elif dartResult[num] == 'D':
                    stack.append(stack.pop() ** 2)
                else: # dartResult[num] == 'T'
                    stack.append(stack.pop() ** 3)
            elif dartResult[num] in '#*':
                if dartResult[num] == '*':
                    temp = stack.pop() * 2
                    if len(stack) >= 1:
                        stack.append(stack.pop() * 2)
                    stack.append(temp)
                else: # '#'
                    stack.append(stack.pop() * (-1))
    return sum(stack)