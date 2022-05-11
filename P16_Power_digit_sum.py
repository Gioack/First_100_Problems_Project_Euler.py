def Power_digit_sum():
    x = 2**1000
    Sum_digit = 0
    for i in str(x):
        Sum_digit += int(i)
    return Sum_digit
print(Power_digit_sum())