from fractions import Fraction


class digit_cancelling_fractions():
    def solution(self):
        cancelling_fractions = self.get_set_of_cancelling_fractions()
        product_fractions = 1
        for numerator, denominator in cancelling_fractions:
            product_fractions *= Fraction(numerator, denominator)
        return product_fractions.denominator

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


print(digit_cancelling_fractions().solution())
