def solution():
    for _ in range(int(input())):
        stack = []
        switch = False
        for item in input():
            if item == "(":
                stack.append("(")
            elif item == ")":
                if stack:
                    stack.pop()
                # 비어있을 경우
                else:
                    print("NO")
                    switch = True
                    break
        # 비어있을 경우
        if switch:
            continue
        
        if stack:
            print("NO")
        else:
            print("YES")


solution()
