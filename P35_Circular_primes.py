from sympy import primerange, isprime


class circular_primes():
    def check_permutations(self):
        circular_primes_number = set()
        for prime in primerange(1000000):
            if self.is_circular(prime) == True:
                circular_primes_number.add(prime)
        return len(circular_primes_number)

    def is_circular(self, number):
        cyclic_permutations = self.get_cyclic_permutations(number)
        for number in cyclic_permutations:
            if isprime(int(number)) == False:
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


print(circular_primes().check_permutations())
