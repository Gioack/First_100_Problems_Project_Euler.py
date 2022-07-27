def powerful_digit_counts():
    counter_number_of_this_kind = 0
    for n in range(1, 10):
        exponent = 1
        power_of_n = n**exponent
        while True:
            if len(str(power_of_n)) == exponent:
                counter_number_of_this_kind += 1
            else:
                break
            exponent += 1
            power_of_n = n**exponent
    return counter_number_of_this_kind


print(powerful_digit_counts())
