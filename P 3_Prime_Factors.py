from sympy.ntheory import factorint


def largest_prime_factor():
    number = 600851475143
    all_factors = factorint(number)
    return max(all_factors)


print(largest_prime_factor())
