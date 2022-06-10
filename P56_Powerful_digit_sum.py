def powerful_digit_sum():
    biggest_sum_digits = 0
    for a in range(1, 101):
        for b in range(1, 101):
            sum_digits = calculate_sum_digits(a**b)
            if sum_digits > biggest_sum_digits:
                biggest_sum_digits = sum_digits
    return biggest_sum_digits


def calculate_sum_digits(number):
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)
    return sum_digits


print(powerful_digit_sum())
