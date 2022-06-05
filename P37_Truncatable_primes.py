from sympy import primerange, isprime


class truncatable_primes():
    def get_sum_of_truncable_primes(self):
        sum_truncable_primes = list()
        for prime in primerange(1000000):
            if prime < 10:
                continue
            if self.is_truncable(prime):
                sum_truncable_primes.append(prime)
        return sum(sum_truncable_primes)

    def is_truncable(self, number):
        return (self.is_truncable_from_left(number)) and (self.is_truncable_from_right(number))

    def is_truncable_from_left(self, number):
        while number != "":
            if isprime(int(number)) == False:
                return False
            number = str(number)[1:]
        return True

    def is_truncable_from_right(self, number):
        while number != "":
            if isprime(int(number)) == False:
                return False
            number = str(number)[:-1]
        return True


print(truncatable_primes().get_sum_of_truncable_primes())
