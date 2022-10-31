def solution(s):
    s = s.lower()
    p = s.count('p')
    y = s.count('y')
    if p == 0 and y == 0:
        return True
    return True if p == y else False