from collections import Counter


def is_prime(num):
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True


def get_smallest_prime_divisor(number):
    divisor_prime = 2
    while number % divisor_prime != 0:
        divisor_prime += 1
        while not is_prime(divisor_prime):
            divisor_prime += 1
    return divisor_prime


def get_prime_factors(number):
    prime_factors = list()
    while number != 1:
        smallest_prime_divisor = get_smallest_prime_divisor(number)
        number /= smallest_prime_divisor
        prime_factors.append(smallest_prime_divisor)
    return Counter(prime_factors)


def largest_prime_factor():
    number = 600851475143
    all_factors = get_prime_factors(number).keys()
    return max(all_factors)


print(largest_prime_factor())
