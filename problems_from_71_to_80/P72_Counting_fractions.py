from sympy.ntheory import factorint


def counting_fractions():
    number_of_fractions = 0
    for n in range(2, 1000001):
        # Look at problem 69 to understand totien
        totien_function_result = totien_function(n)
        number_of_fractions += totien_function_result
    return int(number_of_fractions)


def totien_function(n):
    result = n
    prime_factors = (factorint(n))
    for prime in set(prime_factors):
        result *= (1-1/prime)
    return result


print(counting_fractions())
