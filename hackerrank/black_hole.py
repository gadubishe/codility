__author__ = 'ask'


def mult(a, b, m):
    return ((a % m) * (b % m)) % m


def sum(a, b, m):
    return ((a % m) + (b % m)) % m


def modular_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result

def calculate_sum(n, a, b, M):
    s = 0
    for k in xrange(n+1):
        s += mult(modular_pow(k, a, M), modular_pow(b, k, M), M) % M
        s = s % M
    return s

N = input()
for i in xrange(N):
    n, a, b, M = map(int, raw_input().split(' '))
    print calculate_sum(n, a, b, M)

# def pow_m(a, p, m):
#     a = a % m
#     if p == 0:
#         return 1
#     if p == 1:
#         return a
#
#     c = 1
#     a_k = a
#     while (c < p) and (a_k != a):
#         a_k *= a
#         c += 1
#