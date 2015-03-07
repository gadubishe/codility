__author__ = 'ask'

def solution(S):
    opened = 0
    for e in S:
        if e == '(':
            opened += 1
        else:
            opened -= 1
        if opened < 0:
            return 0
    return 1 if opened == 0 else 0