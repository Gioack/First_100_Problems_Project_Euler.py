def power_digit_sum():
    x = 2**1000
    sum_digits = 0
    for i in str(x):
        sum_digits += int(i)
    return sum_digits


print(power_digit_sum())
