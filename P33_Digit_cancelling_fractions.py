def calculate_wrongly_simplified_fraction(numerator, denominator, common_digit):
    numerator_without_common_digit = str(numerator).replace(
        common_digit, "")
    denominator_without_common_digit = str(
        denominator).replace(common_digit, "")
    try:
        fraction_wrongly_simplified = int(numerator_without_common_digit) / \
            int(denominator_without_common_digit)
    except (ValueError, ZeroDivisionError):
        return False
    return fraction_wrongly_simplified


def is_cancelling_fraction(numerator, denominator):
    for digit in str(numerator):
        if digit == "0":
            return False
        if digit in str(denominator):
            fraction_wrongly_simplified = calculate_wrongly_simplified_fraction(
                numerator, denominator, digit)
            if numerator/denominator == fraction_wrongly_simplified:
                return True
    return False


def get_set_of_cancelling_fractions():
    cancelling_fractions = set()
    for numerator in range(10, 100):
        for denominator in range(10, 100):
            if is_cancelling_fraction(numerator, denominator):
                if (numerator != denominator) and ((denominator, numerator) not in cancelling_fractions):
                    cancelling_fractions.add((numerator, denominator))
    return cancelling_fractions


def reduce_these_fractions(cancelling_fractions):
    cancelling_fractions_at_lowest_terms = list()
    for numerator, denominator in cancelling_fractions:
        denominator = denominator/numerator
        numerator = 1
        cancelling_fractions_at_lowest_terms.append([numerator, denominator])
    return cancelling_fractions_at_lowest_terms


def get_denominator_of_cancelling_fractions_product_lowest_term():
    cancelling_fractions = get_set_of_cancelling_fractions()
    cancelling_fractions = reduce_these_fractions(cancelling_fractions)
    numerators_product = 1
    denominators_product = 1
    for numerator, denominator in cancelling_fractions:
        numerators_product *= numerator
        denominators_product *= denominator
    return denominators_product/numerators_product


print(get_denominator_of_cancelling_fractions_product_lowest_term())
