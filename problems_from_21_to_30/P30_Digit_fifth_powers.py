def digit_fifth_powers():
    sum_of_numbers_that_can_be_written_as_the_sum_of_fifth_powers_of_their_digits = 0
    for number in range(2, 1000000):
        sum_of_fith_powers_of_digits = get_sum_of_the_fifth_powers_of_each_digits(
            number)
        if sum_of_fith_powers_of_digits == number:
            sum_of_numbers_that_can_be_written_as_the_sum_of_fifth_powers_of_their_digits += sum_of_fith_powers_of_digits
    return sum_of_numbers_that_can_be_written_as_the_sum_of_fifth_powers_of_their_digits


def get_sum_of_the_fifth_powers_of_each_digits(number):
    sum_of_fith_power_of_digits = 0
    for digit in str(number):
        sum_of_fith_power_of_digits += int(digit)**5
    return sum_of_fith_power_of_digits


print(digit_fifth_powers())
