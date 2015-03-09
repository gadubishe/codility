__author__ = 'ask'

def kadane(l):
    max_ending_here = max_so_far = l[0]
    for i in xrange(1, len(l)):
        max_ending_here = max(0, max_ending_here+l[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_subset(l):
    s = sum((max(0, x) for x in l))
    return s if s != 0 else max(l)

tests_number = input()
for t in xrange(tests_number):
    n = input()
    l = map(int, raw_input().split())
    print ' '.join([str(kadane(l)), str(max_subset(l))])