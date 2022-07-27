from math import factorial


def digit_factorials():
    factorials_value = [factorial(x) for x in range(10)]
    sum_numbers_are_digit_factorials = 0
    for number in range(3, 2500000):
        sum_digit_factorials = 0
        for digit in str(number):
            sum_digit_factorials += factorials_value[int(digit)]
        if sum_digit_factorials == number:
            sum_numbers_are_digit_factorials += number
    return sum_numbers_are_digit_factorials


print(digit_factorials())
