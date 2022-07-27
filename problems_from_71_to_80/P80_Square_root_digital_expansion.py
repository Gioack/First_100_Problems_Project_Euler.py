from decimal import *
getcontext().prec = 102


def square_root_digital_expansion():
    total_all_digits = 0
    for x in range(1, 101):
        square_root_x = Decimal(str(x)).sqrt()
        if float(square_root_x).is_integer():
            continue
        total_all_digits += get_sum_of_first_100_decimal_digits(square_root_x)
    return total_all_digits


def get_sum_of_first_100_decimal_digits(number):
    sum_of_first_100_decimal_digits = int(str(number)[0])
    decimal_part = number % 1
    for x in str(decimal_part)[2:-2]:
        sum_of_first_100_decimal_digits += int(x)
    return sum_of_first_100_decimal_digits


if __name__ == "__main__":
    print(square_root_digital_expansion())
