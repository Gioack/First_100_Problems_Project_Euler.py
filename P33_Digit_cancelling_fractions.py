class digit_cancelling_fractions():
    def solution(self):
        cancelling_fractions = self.get_set_of_cancelling_fractions()
        # the following code is based on the values of the fractions, it wouldn't work if the values were different
        cancelling_fractions = self.reduce_these_fractions(
            cancelling_fractions)
        numerator, denominator = self.multiply_fractions_and_reduce(
            cancelling_fractions)
        return denominator

    def get_set_of_cancelling_fractions(self):
        cancelling_fractions = set()
        for denominator in range(10, 100):
            for numerator in range(10, denominator):
                if self.is_cancelling_fraction(numerator, denominator):
                    cancelling_fractions.add((numerator, denominator))
        return cancelling_fractions

    def is_cancelling_fraction(self, numerator, denominator):
        numerator, denominator = str(numerator), str(denominator)
        if ("0" in denominator):
            return False
        if (numerator[0] == numerator[1]) or (denominator[0] == denominator[1]):
            return False
        for digit in numerator:
            if digit in denominator:
                fraction_wrongly_simplified = self.calculate_wrongly_simplified_fraction(
                    numerator, denominator, digit)
                if int(numerator)/int(denominator) == fraction_wrongly_simplified:
                    return True
        return False

    def calculate_wrongly_simplified_fraction(self, numerator, denominator, common_digit):
        numerator_without_common_digit, denominator_without_common_digit = self.delete_commmon_digits_fraction(
            numerator, denominator, common_digit)
        fraction_wrongly_simplified = int(
            numerator_without_common_digit) / int(denominator_without_common_digit)
        return fraction_wrongly_simplified

    def delete_commmon_digits_fraction(self, numerator, denominator, common_digit):
        numerator_without_common_digit = numerator.replace(
            common_digit, "")
        denominator_without_common_digit = denominator.replace(
            common_digit, "")
        return numerator_without_common_digit, denominator_without_common_digit

    def reduce_these_fractions(self, cancelling_fractions):
        cancelling_fractions_at_lowest_terms = list()
        for numerator, denominator in cancelling_fractions:
            denominator = denominator/numerator
            numerator = 1
            cancelling_fractions_at_lowest_terms.append(
                [numerator, denominator])
        return cancelling_fractions_at_lowest_terms

    def multiply_fractions_and_reduce(self, fractions):
        numerators_product = 1
        denominators_product = 1
        for numerator, denominator in fractions:
            numerators_product *= numerator
            denominators_product *= denominator
        return 1, int(denominators_product/numerators_product)


s = digit_cancelling_fractions()
print(s.solution())
