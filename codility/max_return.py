__author__ = 'ask'

def kadane_algorithm(l):
	max_ending_here = max_so_far = 0
	for x in l:
		max_ending_here = max(0, max_ending_here + x)
		max_so_far = max(max_so_far, max_ending_here)
	return max_so_far

def solution(A):
	return kadane_algorithm((A[i] - A[i-1] for i in xrange(1, len(A))))