from itertools import permutations


def sub_string_divisibility():
    sum_pandigitalas_with_this_property = 0
    all_pandigitals_0_to_10 = permutations([x for x in range(10)])
    for pandigital_0_to_10 in all_pandigitals_0_to_10:
        if pandigital_0_to_10[0] == 0:
            continue
        if has_divisibility_property(pandigital_0_to_10):
            sum_pandigitalas_with_this_property += convert_tuple_to_int(
                pandigital_0_to_10)
    return sum_pandigitalas_with_this_property


def has_divisibility_property(number):
    number = convert_tuple_to_str(number)
    a = 1
    for x in [2, 3, 5, 7, 11, 13, 17]:
        considered_digits = int(number[a:a+3])
        if considered_digits % x != 0:
            return False
        a += 1
    return True


def convert_tuple_to_int(tuple):
    return int("".join((str(v) for v in tuple)))


def convert_tuple_to_str(tuple):
    return "".join((str(v) for v in tuple))


print(sub_string_divisibility())
