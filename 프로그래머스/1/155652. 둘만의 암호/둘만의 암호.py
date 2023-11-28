def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in range(len(skip)):
        if skip[i] in alpha:
            alpha = alpha.replace(skip[i], "")
    
    for c in s:
        answer += alpha[(alpha.find(c) + index)%len(alpha)] 
    return answer