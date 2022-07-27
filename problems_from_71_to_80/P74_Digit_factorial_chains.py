from math import factorial


def digit_factorial_chains():
    number_of_chain_with_lenght_60 = 0
    for x in range(1000000):
        if get_lenght_chain(x) == 60:
            number_of_chain_with_lenght_60 += 1
    return number_of_chain_with_lenght_60


def get_lenght_chain(x):
    chain = list()
    sum_factorial_digits = get_sum_sum_factorial_digits(x)
    chain.append(x)
    while sum_factorial_digits not in chain:
        chain.append(sum_factorial_digits)
        sum_factorial_digits = get_sum_sum_factorial_digits(
            sum_factorial_digits)
    return len(chain)


def get_sum_sum_factorial_digits(number):
    sum_factorial_digits = 0
    for digit in str(number):
        sum_factorial_digits += factorial(int(digit))
    return sum_factorial_digits


print(digit_factorial_chains())
