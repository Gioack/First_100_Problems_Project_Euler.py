from itertools import combinations
from sympy import primerange


class prime_digit_replacement():
    primes_as_bools = []

    def __init__(self):
        self.add_primes_eratosthenes_sieve(1000000)

    def get_result(self):
        for prime in primerange(200000):
            for family in self.create_all_families(prime):
                only_primes_family = list(
                    filter(self.respects_criteria, family))
                number_of_primes_in_family = len(only_primes_family)
                if number_of_primes_in_family == 8:
                    return min(only_primes_family)

    def create_all_families(self, number):
        families = list()
        number = str(number)
        for mask in self.get_all_possible_masks(number):
            family = self.create_family(number, mask)
            families.append(family)
        return families

    def get_all_possible_masks(self, number):
        number = str(number)
        masks = list()
        for n in range(1, len(number)):
            for masks_with_n_digits_masked in combinations(range(len(number)), n):
                masks.append(list(masks_with_n_digits_masked))
        return masks

    def create_family(self, number, mask):
        family = list()
        for number_for_replacing in range(0, 10):
            number_replaced = number
            for index in mask:
                number_replaced = number_replaced.replace(
                    number_replaced[index], str(number_for_replacing))
            family.append(number_replaced)
        return family

    def respects_criteria(self, num):
        return self.is_number_without_zeros_at_the_beginning(num) and self.is_prime(num)

    def is_number_without_zeros_at_the_beginning(self, num):
        return str(int(num)) == num

    def is_prime(self, num):
        num = int(num)
        return self.primes_as_bools[num]

    def add_primes_eratosthenes_sieve(self, until):
        self.primes_as_bools = [True for i in range(until + 1)]
        p = 2
        while (p * p <= until):
            if (self.primes_as_bools[p] == True):
                for i in range(p ** 2, until + 1, p):
                    self.primes_as_bools[i] = False
            p += 1
        self.primes_as_bools[0] = False
        self.primes_as_bools[1] = False


s = prime_digit_replacement()
print(s.get_result())
