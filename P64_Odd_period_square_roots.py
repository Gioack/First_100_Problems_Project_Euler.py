from math import floor, sqrt


def odd_period_square_roots():
    counter = 0
    for x in range(2, 10001):
        if calculate_length_period(x) % 2 == 1:
            counter += 1
    return counter


def calculate_length_period(n):
    """
    This function relies on a math formula, you can learn more
    about it here: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion 
    """
    length_period = 0
    root_n = sqrt(n)
    if is_perfect_root(root_n):
        return length_period
    integer_part = get_integer_part(root_n)
    numerator = 0.0
    denominator = 1.0
    leading_coefficient = integer_part
    while integer_part != 2*leading_coefficient:
        numerator = denominator * integer_part - numerator
        denominator = (n - numerator ** 2) / denominator
        integer_part = get_integer_part((root_n + numerator) / denominator)
        length_period += 1
    return length_period


def get_integer_part(root_n):
    return floor(root_n)


def is_perfect_root(root):
    return int(root) == root


print(odd_period_square_roots())
