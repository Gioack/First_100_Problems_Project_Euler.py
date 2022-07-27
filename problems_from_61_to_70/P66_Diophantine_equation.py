from math import floor, sqrt


def calculate_continued_fraction(n):
    """
    This function relies on a math formula, you can learn more
    about it here: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion 
    """
    root_n = sqrt(n)
    if is_perfect_root(root_n):
        return 0
    integer_part = get_integer_part(root_n)
    convergents = [integer_part]
    numerator = 0.0
    denominator = 1.0
    leading_coefficient = integer_part
    while integer_part != 2*leading_coefficient:
        numerator = denominator * integer_part - numerator
        denominator = (n - numerator ** 2) / denominator
        integer_part = get_integer_part((root_n + numerator) / denominator)
        convergents.append(integer_part)
    convergents.pop()
    return convergents


def get_integer_part(root_n):
    return floor(root_n)


def is_perfect_root(root):
    return int(root) == root


def calculate_starting_number(continued_fraction):
    numerator = 1
    denominator = continued_fraction.pop()
    while continued_fraction:
        denominator, numerator = denominator * \
            continued_fraction.pop() + numerator, denominator
    return denominator, numerator


def main():
    largest = 0, 0
    for i in range(1, 1001):
        if i % sqrt(i) != 0:
            continued_fraction = calculate_continued_fraction(i)
            if len(continued_fraction) % 2 != 0:
                u, v = calculate_starting_number(continued_fraction)
                u, v = 2*u**2+1, 2*u*v
            else:
                u, v = calculate_starting_number(continued_fraction)
            if u > largest[1]:
                largest = i, u
    return largest[0]


print(main())
