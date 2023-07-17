def solution():
    for _ in range(int(input())):
        nums, idx = map(int, input().split())
        queue = list(map(int, input().split()))

        value = queue[idx]
        cnt = 1
        while queue:
            # 목표 숫자라면
            if idx == 0:
                # 최대 값일 경우 -> 출력
                if value >= max(queue):
                    print(cnt)
                    break
                # 최대 값이 아닐 경우 -> 다시 뒤로
                else:
                    queue.append(queue.pop(0))
                    idx = len(queue) - 1
            # 목표 숫자가 아닐 경우
            else:
                num = queue.pop(0)
                if num >= max(queue):
                    cnt += 1
                else:
                    queue.append(num)
                idx -= 1


solution()
