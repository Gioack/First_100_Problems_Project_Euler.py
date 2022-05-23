def get_factorial(num):
    factorial = 1
    if num == 0:
        return factorial
    for i in range(2, num+1):
        factorial *= i
    return factorial


def digit_factorials():
    factorials_value = [get_factorial(x) for x in range(10)]
    sum_numbers_are_digit_factorials = 0
    for number in range(3, 2500000):
        sum_digit_factorials = 0
        for digit in str(number):
            sum_digit_factorials += factorials_value[int(digit)]
        if sum_digit_factorials == number:
            sum_numbers_are_digit_factorials += number
    return sum_numbers_are_digit_factorials


print(digit_factorials())
