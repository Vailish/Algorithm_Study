def solution(name, yearning, photo):
    answer = []
    for pic in photo:
        pnt = 0        
        for target in pic:
            if target in name:
                pnt += yearning[name.index(target)]
        answer.append(pnt)
    return answer