from math import factorial


def factorial_digit_sum():
    digit_sum = 0
    for digit in str(factorial(100)):
        digit_sum += int(digit)
    return digit_sum


print(factorial_digit_sum())
