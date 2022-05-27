from itertools import permutations


class pandigital_prime():
    primes = [2]

    def pandigital_prime(self):
        for i in reversed(range(10)):
            all_pandigitals_1_to_i = permutations([x for x in range(1, i)])
            pandigital_primes = list()
            for permutation in all_pandigitals_1_to_i:
                permutation = self.convert_tuple_to_int(permutation)
                if self.is_prime(permutation):
                    pandigital_primes.append(permutation)
            if pandigital_primes:
                return max(pandigital_primes)

    def convert_tuple_to_int(self, tuple):
        return int("".join((str(v) for v in tuple)))

    def is_prime(self, num):
        for n in range(2, int(num**0.5)+1):
            if num % n == 0:
                return False
        return True


s = pandigital_prime()
print(s.pandigital_prime())
