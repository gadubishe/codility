__author__ = 'ask'

mod = 100


def modular_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result


def precalculate(N, K):
    return [modular_pow(i, N, mod) for i in xrange(0, min(mod, K + 1))]


def calculate_sum(powers_mod, K):
    return (((K / mod) * (sum(powers_mod) % mod)) % mod + sum(powers_mod[:(K % mod) + 1]) % mod) % mod


# n = 3
# k = 2
#
# pre = precalculate(n, k)
# print calculate_sum(pre, k)

N = input()
for i in xrange(N):
    k, n = map(int, raw_input().split(' '))
    print str(calculate_sum(precalculate(n, k), k)).zfill(2)

# if __name__ == '__main__':
#     N = 1000000000000000
#     print N
#     print precalculate(N)