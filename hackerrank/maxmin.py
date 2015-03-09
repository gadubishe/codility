import sys


def maxmin(candies, k):
    candies.sort()
    min_unfairness = sys.maxint
    for i in xrange(len(candies) - k):
        min_unfairness = min(min_unfairness, candies[i + k - 1] - candies[i])
    return min_unfairness


n = input()
k = input()
candies = [input() for _ in xrange(n)]

min_diff = maxmin(candies, k)

print min_diff