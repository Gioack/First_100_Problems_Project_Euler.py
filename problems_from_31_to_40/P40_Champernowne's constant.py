def champernowne_s_constant():
    digit_counter = 0
    product = 1
    wanted_digits = [int(10**x) for x in range(7)]
    for x in range(1, 1000001):
        for digit in str(x):
            digit = int(digit)
            digit_counter += 1
            if digit_counter in wanted_digits:
                product *= digit
    return product


print(champernowne_s_constant())
