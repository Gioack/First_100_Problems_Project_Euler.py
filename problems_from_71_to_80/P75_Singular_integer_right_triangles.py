from collections import Counter
from math import ceil, sqrt


def eratosthenes_sieve(N):
    N += 1
    spf = [*range(N)]
    for i in range(4, N, 2):
        spf[i] = 2
    for i in range(3, ceil(sqrt(N))):
        if (spf[i] == i):
            for j in range(i * i, N, i):
                if (spf[j] == j):
                    spf[j] = i
    return spf


def get_reduced_factorization(N, spf):
    gamma = 1
    while (N != 1):
        prev = spf[N]
        c = 0
        while spf[N] == prev:
            c += 1
            N //= spf[N]
        gamma *= pow(prev, ceil(c/2))
        prev = spf[N]
    return gamma


def pythagorean_triplets(n):
    all_triplets_sum = list()
    spf = eratosthenes_sieve((n - int(sqrt((n << 1) - 1))) << 1)
    for b2 in range(4, (n - int(sqrt((n << 1) - 1))) << 1, 2):
        gamma = get_reduced_factorization(b2, spf)
        for i in range(1, int(sqrt(b2*((b2 >> 1)-1)))//gamma+1):
            i *= gamma
            sqVal = i*i
            q = sqVal//b2
            if q+i+(b2 >> 1) > n:
                break
            else:
                x = q+i
                sum_numbers = sum([x, (b2 >> 1)+i, x+(b2 >> 1)])
                if sum_numbers <= 1500000:
                    all_triplets_sum.append(sum_numbers)
    return len({k: v for k, v in Counter(all_triplets_sum).items() if v == 1})


print(pythagorean_triplets(1500000))
