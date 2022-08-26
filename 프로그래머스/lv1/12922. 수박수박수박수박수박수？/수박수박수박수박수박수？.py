import itertools

def solution(n):
    a = itertools.cycle("수박")
    return ''.join([a.__next__() for i in range(n)])