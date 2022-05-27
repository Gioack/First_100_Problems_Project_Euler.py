class circular_primes():
    primes_as_bools = []

    def check_permutations(self):
        circular_primes_number = set()
        for prime, bool in enumerate(self.primes_as_bools):
            if bool == True:
                if self.is_circular(prime) == True:
                    circular_primes_number.add(prime)
        return len(circular_primes_number)

    def is_circular(self, number):
        cyclic_permutations = self.get_cyclic_permutations(number)
        for number in cyclic_permutations:
            if self.is_prime(number) == False:
                return False
        return True

    def get_cyclic_permutations(self, number):
        cyclic_permutations = list()
        number = str(number)
        original_number = number
        number = f"{number[1:]}{number[0]}"
        cyclic_permutations.append(number)
        while number != original_number:
            number = f"{number[1:]}{number[0]}"
            cyclic_permutations.append(number)
        return cyclic_permutations

    def add_primes(self, until):
        self.primes_as_bools = [True for i in range(until + 1)]
        p = 2
        while (p * p <= until):
            if (self.primes_as_bools[p] == True):
                for i in range(p ** 2, until + 1, p):
                    self.primes_as_bools[i] = False
            p += 1
        self.primes_as_bools[0] = False
        self.primes_as_bools[1] = False

    def is_prime(self, num):
        return self.primes_as_bools[int(num)]


s = circular_primes()
s.add_primes(1000000)
print(s.check_permutations())
