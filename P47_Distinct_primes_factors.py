from sympy.ntheory import factorint


def distinct_primes_factors():
    number = 10
    counter = 0
    while True:
        prime_factors = factorint(number)
        if len(prime_factors) != 4:
            counter = 0
        else:
            counter += 1
        if counter == 4:
            return number-3
        number += 1


print(distinct_primes_factors())
