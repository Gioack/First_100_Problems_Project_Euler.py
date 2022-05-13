def get_summation(num):
    summation = 1
    for i in range(2,num+1):
        summation *= i
    return summation


def factorial_digit_sum():
    digit_sum = 0
    for digit in str(get_summation(100)):
        digit_sum += int(digit)
    return digit_sum


print(factorial_digit_sum())