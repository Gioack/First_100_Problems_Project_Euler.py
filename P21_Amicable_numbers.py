from sympy import divisors


def amicable_numbers():
    sum_amicable = 0
    for number in range(1, 10000):
        sum_of_divisors_of_number = sum_of_divisors(number)
        if number == sum_of_divisors_of_number:
            continue
        sum_divisors_of_sum_divisors_of_number = sum_of_divisors(
            sum_of_divisors_of_number)
        if number == sum_divisors_of_sum_divisors_of_number:
            sum_amicable += (number+sum_of_divisors_of_number)
    sum_amicable_counting_once_each_pair = sum_amicable / 2
    return int(sum_amicable_counting_once_each_pair)


def sum_of_divisors(number):
    return sum(divisors(number))-number


print(amicable_numbers())
