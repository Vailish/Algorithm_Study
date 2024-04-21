def solution(keymap, targets):
    answer = []
    # 가능성 여부 확인
    for target in targets:
        cnt = 0
        for char in target:
            time = 100
            is_success = False

            for key in keymap:
                if char in key:
                    time = min(key.index(char)+1, time)
                    is_success = True
            if not is_success:
                cnt = -1
                break
            cnt += time
            
        answer.append(cnt)
                
    return answer