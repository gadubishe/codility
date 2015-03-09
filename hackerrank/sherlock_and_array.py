__author__ = 'ask'

def check(l):
    N = len(l)
    if N == 1:
        return True

    left_sum = [0]*len(l)
    s = 0
    for i in xrange(1, N):
        s += l[i-1]
        left_sum[i] = s

    right_sum = [0]*len(l)
    s = 0

    for i in xrange(N-2, -1, -1):
        s += l[i+1]
        right_sum[i] = s
    for (left, right) in zip(left_sum, right_sum):
        if left == right:
            return True
    return False

N = input()
for i in xrange(N):
    length = input()
    print 'YES' if check(map(int, raw_input().split(' '))) else 'NO'
