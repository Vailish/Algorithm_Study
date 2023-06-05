def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        # 스킬트리
        # 하나씩 빼서 확인 후 해당 값이 있다면 추가해줌
        tmp = ""
        for tree in skill_tree:       
            if tree in skill:         # 스킬트리 중에 skill이 있다면 s에 추가
                tmp += tree
        # tmp가 skill과 같다면 answer += 1
        if skill[:len(tmp)] == tmp:     
            answer += 1
    
    return answer