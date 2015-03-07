__author__ = 'ask'
def b_pair(s):
    return '(' if s == ')' else '[' if s == ']' else '{' if s == '}' else None

def solution(s):
    l = []
    for e in s:
        if e in ['(', '[', '{']:
            l.append(e)
        else:
            if len(l) == 0:
                return 0
            lastOpened = l.pop()
            if lastOpened != b_pair(e):
                return 0
    return 1 if not l else 0