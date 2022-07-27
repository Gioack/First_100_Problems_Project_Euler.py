from sympy.ntheory import factorint


def totient_maximum():
    biggest_quotient = 2
    n_of_biggest_quotient = 0
    for n in range(2, 10**6):
        totien_function_result = totien_function(n)
        if n/totien_function_result > biggest_quotient:
            biggest_quotient = n/totien_function_result
            n_of_biggest_quotient = n
    return n_of_biggest_quotient


def totien_function(n):
    result = n
    prime_factors = factorint(n)
    for prime in set(prime_factors):
        result *= (1-1/prime)
    return result


print(totient_maximum())
