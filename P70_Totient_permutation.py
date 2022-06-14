from collections import Counter
from math import sqrt


class totient_permutation():
    prime_factors_of_each_number = dict()

    def main(self):
        smallest_result = None
        n_smallest_result = None
        for n in range(2, 10**7):
            totien_function_result = self.totien_function(n)
            if (smallest_result == None) or ((self.are_permutations(n, totien_function_result)) and ((n/totien_function_result) < smallest_result)):
                smallest_result = n/totien_function_result
                n_smallest_result = n
        return n_smallest_result

    def totien_function(self, n):
        totien_function_result = n
        prime_factors = (self.get_prime_factors(n))
        for prime in set(prime_factors):
            totien_function_result *= (1-1/prime)
        return int(totien_function_result)

    def get_prime_factors(self, n):
        prime_factors = list()
        original_n = n
        while n % 2 == 0:
            prime_factors.append(2)
            n = n / 2
            if n in self.prime_factors_of_each_number:
                self.prime_factors_of_each_number[original_n] = self.prime_factors_of_each_number[n]+prime_factors
                return self.prime_factors_of_each_number[original_n]
        for i in range(3, int(sqrt(n))+1, 2):
            while n % i == 0:
                prime_factors.append(i)
                n = n / i
                if n in self.prime_factors_of_each_number:
                    self.prime_factors_of_each_number[original_n] = self.prime_factors_of_each_number[n]+prime_factors
                    return self.prime_factors_of_each_number[original_n]
        if n > 2:
            prime_factors.append(n)
        self.prime_factors_of_each_number[original_n] = prime_factors
        return self.prime_factors_of_each_number[original_n]

    def are_permutations(self, a, b):
        return Counter(str(a)) == Counter(str(b))


print(totient_permutation().main())
