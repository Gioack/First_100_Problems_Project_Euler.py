def powerful_digit_counts():
    number_of_this_kind = 0
    for x in range(1, 1000):
        counter_1 = 0
        counter_2 = 0
        i = 0
        power = x**i
        while True:
            if len(str(power)) <= i:
                counter_1 += 1
                counter_2 = 0
            if len(str(power)) >= i:
                counter_2 += 1
                counter_1 = 0
            if (counter_1 > 2) or (counter_2 > 2):
                break
            if len(str(power)) == i:
                number_of_this_kind += 1
            i += 1
            power = x**i
    return number_of_this_kind


print(powerful_digit_counts())
